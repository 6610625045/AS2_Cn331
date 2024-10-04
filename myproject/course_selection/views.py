from django.shortcuts import render
from courses.models import Course
from django.contrib.auth.decorators import login_required

def course_list(request):
    courses = Course.objects.all()  # ดึงข้อมูลวิชาทั้งหมด
    return render(request, 'course_selection/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course_selection/course_detail.html', {'course': course})

def course_selection_home(request):
    courses = Course.objects.filter(enrollment_status=True)  # ดึงเฉพาะวิชาที่เปิดรับ
    return render(request, 'course_selection/course_selection_home.html')

