# courses/admin.py

from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_name', 'semester', 'academic_year', 'max_capacity', 'enrollment_status')
    search_fields = ('course_name', 'course_code')
    list_filter = ('semester', 'enrollment_status')
