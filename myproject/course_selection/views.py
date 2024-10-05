from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Course
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, CourseRegistration

# แสดงรายการวิชาทั้งหมด
def course_list(request):
    courses = Course.objects.all()  # ดึงข้อมูลวิชาทั้งหมด
    return render(request, 'course_selection/course_list.html', {'courses': courses})

# แสดงรายละเอียดวิชา
def course_detail(request, course_code):
    course = get_object_or_404(Course, course_code=course_code)
    return render(request, 'course_selection/course_detail.html', {'course': course})

# แสดงหน้าหลักสำหรับการเลือกวิชา
def course_selection_home(request):
    # ดึงข้อมูลวิชาทั้งหมดที่เปิดให้ลงทะเบียนได้
    available_courses = Course.objects.filter(enrollment_status=True)
    
    if request.method == 'POST':
        selected_courses = request.POST.getlist('selected_courses')  # ดึงค่าจาก checkbox ที่ถูกเลือก
        if selected_courses:
            for course_code in selected_courses:
                selected_course = get_object_or_404(Course, course_code=course_code)
                # เพิ่มการบันทึกการลงทะเบียน
                CourseRegistration.objects.create(user=request.user, course=selected_course)
            return redirect('registration_complete')  # พาผู้ใช้ไปยังหน้าลงทะเบียนเสร็จสิ้น
    
    context = {
        'courses': available_courses
    }
    return render(request, 'course_selection/course_selection_home.html', context)

# ฟังก์ชันสำหรับการลงทะเบียนวิชา
@login_required
def course_register(request, course_code):
    course = get_object_or_404(Course, course_code=course_code)
    user = request.user
    CourseRegistration.objects.create(user=user, course=course)
    return redirect('registration_complete')

# แสดงหน้าลงทะเบียนเสร็จสิ้น
def registration_complete(request):
    return render(request, 'course_selection/register_subject_complete.html')
