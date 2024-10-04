from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=20)
    max_capacity = models.IntegerField()
    enrollment_status = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name
    
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.course.course_name}"
