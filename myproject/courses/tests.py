from django.test import TestCase
from .models import Course
from django.contrib.auth.models import User

class CourseModelTest(TestCase):
    
    def setUp(self):
        # สร้างข้อมูลตัวอย่างสำหรับการทดสอบ
        self.course = Course.objects.create(
            course_name="Test Course",
            course_code="TC101",
            semester="1",
            academic_year=2024,
            enrollment_status=True,
            max_capacity=30
        )
    def test_str_method(self):
        # ทดสอบเมธอด __str__ ของ Course (หรือเมธอดอื่น ๆ ที่คุณมี)
        self.assertEqual(str(self.course), "Test Course")

    def test_course_creation(self):
        # ตรวจสอบว่าข้อมูล course ถูกสร้างขึ้นถูกต้อง
        self.assertEqual(self.course.course_name, "Test Course")
        self.assertEqual(self.course.course_code, "TC101")
        self.assertEqual(self.course.semester, "1")
        self.assertEqual(self.course.enrollment_status, True)
        self.assertEqual(self.course.max_capacity, 30)

from django.test import TestCase, Client
from django.urls import reverse

class CourseListViewTests(TestCase):
    def setUp(self):
        self.client = Client()  # สร้าง client สำหรับจำลองคำขอ

    def test_course_list_view(self):
        response = self.client.get(reverse('course_list'))  # เปลี่ยนเป็นชื่อ URL ที่คุณกำหนด
        self.assertEqual(response.status_code, 200)  # ตรวจสอบสถานะ HTTP ว่าต้องเป็น 200
        self.assertTemplateUsed(response, 'course_selection/course_list.html')  # ตรวจสอบว่าใช้เทมเพลตที่ถูกต้อง


