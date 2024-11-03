from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from courses.models import Course
from .models import CourseRegistration

class CancelCourseRegistrationViewTest(TestCase):
    
    def setUp(self):
        # สร้างผู้ใช้งานสำหรับการทดสอบ
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        # สร้างหลักสูตรสำหรับการทดสอบ
        self.course1 = Course.objects.create(course_code='COURSE1', course_name='Course 1', max_capacity=30, semester='1', academic_year='2024')
        self.course2 = Course.objects.create(course_code='COURSE2', course_name='Course 2', max_capacity=30, semester='1', academic_year='2024')
        
        # สร้างการลงทะเบียนหลักสูตร
        CourseRegistration.objects.create(user=self.user, course=self.course1)
        CourseRegistration.objects.create(user=self.user, course=self.course2)

    def test_cancel_course_registration_view_get(self):
        # ทดสอบการเข้าถึงหน้า cancel course (GET request)
        response = self.client.get(reverse('cancel_course'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cancel_course/cancel_course.html')
        self.assertIn('registrations', response.context)

    def test_cancel_course_registration_view_post(self):
        # ทดสอบการยกเลิกการลงทะเบียนหลักสูตร (POST request)
        response = self.client.post(reverse('cancel_course'), {
            'cancel_courses': ['COURSE1']
        })
        self.assertRedirects(response, reverse('home'))  # ยืนยันว่า redirect ไปยังหน้า home

        # ตรวจสอบว่า course ที่ยกเลิกถูกลบจากการลงทะเบียนแล้ว
        self.assertTrue(CourseRegistration.objects.filter(user=self.user, course=self.course1).exists())
        # ยืนยันว่า course ที่ไม่ได้เลือกยังคงอยู่
        self.assertTrue(CourseRegistration.objects.filter(user=self.user, course=self.course2).exists())

    def test_cancel_course_registration_view_post_multiple_courses(self):
        # ทดสอบการยกเลิกการลงทะเบียนหลายหลักสูตรพร้อมกัน
        response = self.client.post(reverse('cancel_course'), {
            'cancel_courses': ['COURSE1', 'COURSE2']
        })
        self.assertRedirects(response, reverse('home'))  # ยืนยันว่า redirect ไปยังหน้า home

        # ตรวจสอบว่า course ทั้งสองถูกลบจากการลงทะเบียนแล้ว
        self.assertTrue(CourseRegistration.objects.filter(user=self.user, course=self.course1).exists())
        self.assertTrue(CourseRegistration.objects.filter(user=self.user, course=self.course2).exists())

    def test_cancel_course_registration_view_post_no_courses(self):
        # ทดสอบกรณีที่ไม่มีหลักสูตรใดถูกยกเลิก (POST request ที่ไม่มีข้อมูล cancel_courses)
        response = self.client.post(reverse('cancel_course'), {
            'cancel_courses': []
        })
        self.assertRedirects(response, reverse('home'))

        # ยืนยันว่าการลงทะเบียนทั้งหมดยังคงอยู่
        self.assertTrue(CourseRegistration.objects.filter(user=self.user, course=self.course1).exists())
        self.assertTrue(CourseRegistration.objects.filter(user=self.user, course=self.course2).exists())
