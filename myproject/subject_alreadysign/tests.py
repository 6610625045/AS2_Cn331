from django.test import TestCase
from django.contrib.auth.models import User
from courses.models import Course
from .models import SubjectRegistration

class SubjectRegistrationModelTest(TestCase):

    def setUp(self):
        # สร้างผู้ใช้และคอร์สเพื่อใช้ในการทดสอบ
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.course = Course.objects.create(course_name='Test Course', course_code='TC101', semester='1', academic_year='2024', max_capacity=30, enrollment_status=True)

    def test_create_subject_registration(self):
        # สร้าง SubjectRegistration
        registration = SubjectRegistration.objects.create(user=self.user, course=self.course)
        # ตรวจสอบว่าการสร้าง SubjectRegistration สำเร็จ
        self.assertEqual(registration.user, self.user)
        self.assertEqual(registration.course, self.course)

    def test_subject_registration_str(self):
        # สร้าง SubjectRegistration
        registration = SubjectRegistration.objects.create(user=self.user, course=self.course)
        # ตรวจสอบว่า __str__ ฟังก์ชันทำงานถูกต้อง
        self.assertEqual(str(registration), 'testuser - Test Course')


from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from course_selection.models import CourseRegistration
from .models import SubjectRegistration
from login_logout.urls import *

class RegisteredCoursesViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        
        # สร้าง Course ที่มีข้อมูลทั้งหมดที่จำเป็น
        self.course = Course.objects.create(course_name='Test Course', course_code='CS101', max_capacity=30, semester='1', academic_year='2024')

        # สร้างการลงทะเบียน
        CourseRegistration.objects.create(user=self.user, course=self.course)

        self.login_logout_url = reverse('login')
    
    def test_registered_courses_view_authenticated(self):
        response = self.client.get(reverse('registered_courses'))  # ใช้ URL ชื่อที่ถูกต้อง
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'subject_alreadysign/subject_sign.html')
