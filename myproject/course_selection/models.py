from django.db import models
from django.contrib.auth.models import User
from courses.models import Course  # นำเข้าโมเดล Course

class CourseRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_selection_user_registrations')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_selection_registrations')
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.course_name}"
