from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Course, CourseRegistration

class CourseSelectionTests(TestCase):

    def setUp(self):
        # สร้างผู้ใช้สำหรับการทดสอบ
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.course1 = Course.objects.create(course_code='CS101', course_name='Course 1', max_capacity=30, semester='1', academic_year='2024', enrollment_status=True)
        self.course2 = Course.objects.create(course_code='CS102', course_name='Course 2', max_capacity=30, semester='1', academic_year='2024', enrollment_status=False)

    def test_course_list_view(self):
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_selection/course_list.html')

    def test_course_detail_view(self):
        response = self.client.get(reverse('course_detail', args=[self.course1.course_code]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_selection/course_detail.html')
        self.assertContains(response, self.course1.course_code)

    def test_course_selection_home_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('course_selection_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_selection/course_selection_home.html')

    def test_course_register_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('course_register', args=[self.course1.course_code]))
        self.assertEqual(response.status_code, 302)  # ตรวจสอบว่า redirect
        self.assertTrue(CourseRegistration.objects.filter(user=self.user, course=self.course1).exists())

    def test_registration_complete_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('registration_complete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course_selection/register_subject_complete.html')

    def test_course_selection_post_valid(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('course_selection_home'), {'selected_courses': [self.course1.course_code]})
        self.assertEqual(response.status_code, 302)  # ตรวจสอบว่า redirect
        self.assertTrue(CourseRegistration.objects.filter(user=self.user, course=self.course1).exists())

    def test_course_selection_post_no_selection(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('course_selection_home'), {'selected_courses': []})
        self.assertEqual(response.status_code, 200)  # ควรกลับไปที่หน้าเลือกวิชา
        self.assertTemplateUsed(response, 'course_selection/course_selection_home.html')

