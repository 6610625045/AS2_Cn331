from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group
from .forms import UserRegisterForm

class RegisterViewTests(TestCase):

    def setUp(self):
        # Create a group for testing
        self.user_group = Group.objects.create(name='User')

    def test_register_user_success(self):
        # Test successful registration
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'TestPassword123',
            'password2': 'TestPassword123',
            'email': 'testuser@example.com'
        })

        # Check if the user was created
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        # Check if the user is added to the 'User' group
        self.assertTrue(self.user_group in user.groups.all())
        # Check if the response redirects to the login page
        self.assertRedirects(response, reverse('login'))

    def test_register_user_invalid(self):
        # Test registration with invalid data (e.g., passwords don't match)
        response = self.client.post(reverse('register'), {
            'username': 'testuser2',
            'password1': 'TestPassword123',
            'password2': 'DifferentPassword123',
            'email': 'testuser2@example.com'
        })

        # Check that the user is not created
        self.assertFalse(User.objects.filter(username='testuser2').exists())
        # Check if the response renders the register page again
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')
        # Check for the specific error message for password mismatch
        self.assertContains(response, "The two password fields didn’t match.")

    def test_register_user_get(self):
        # Test GET request for the registration page
        response = self.client.get(reverse('register'))

        # Check if the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check if the correct template is used
        self.assertTemplateUsed(response, 'account/register.html')
        # Check if the form is present in the response context
        self.assertIsInstance(response.context['form'], UserRegisterForm)
