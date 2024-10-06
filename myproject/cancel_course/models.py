from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class CourseRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cancel_course_user_registrations')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='cancel_course_registrations')
    registration_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f"{self.user.username} - {self.course.course_name}"