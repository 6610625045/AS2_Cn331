# login-logout/tests.py

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class LoginLogoutTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_view(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # ตรวจสอบว่าเปลี่ยนเส้นทางหลังล็อกอิน
        self.assertTrue(response.url.startswith('/home/'))  # ตรวจสอบว่าตรงกับ URL ของหน้าโฮม


    def test_login_view_invalid(self):
        response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)  # ตรวจสอบว่าอยู่ที่หน้าล็อกอิน
        self.assertContains(response, 'Please enter a correct username and password.')  # ตรวจสอบข้อความผิดพลาด

    def test_home_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)  # ตรวจสอบว่าเข้าได้
        self.assertTemplateUsed(response, 'login-logout/home.html')  # ตรวจสอบว่าใช้เทมเพลตที่ถูกต้อง

    def test_home_view_not_authenticated(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)  # ตรวจสอบว่าถูกเปลี่ยนเส้นทาง
        self.assertTrue(response.url.startswith(''))  # ตรวจสอบว่าถูกเปลี่ยนไปยังหน้าล็อกอิน

    def test_login_view_no_post(self):
    # ทดสอบการเข้าเยี่ยมชมหน้าล็อกอินแบบ GET
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)  # ยังคงอยู่ที่หน้าเข้าสู่ระบบ
        self.assertTemplateUsed(response, 'login-logout/login.html')  # ตรวจสอบว่าใช้เทมเพลตที่ถูกต้อง

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # ตรวจสอบว่าล็อกเอาต์แล้วเปลี่ยนเส้นทาง
        self.assertTrue(response.url.startswith(''))  # ตรวจสอบว่าเปลี่ยนไปยังหน้าล็อกอิน
        self.assertNotIn('_auth_user_id', self.client.session)  # ตรวจสอบว่าไม่มีผู้ใช้ล็อกอินอยู่ใน session

    