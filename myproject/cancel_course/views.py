from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Course
from django.contrib.auth.decorators import login_required
from .models import CourseRegistration
from course_selection.models import CourseRegistration

@login_required
def cancel_course_registration(request):
    registrations = CourseRegistration.objects.filter(user=request.user)
    
    if request.method == 'POST':
        selected_courses = request.POST.getlist('cancel_courses')
        for course_code in selected_courses:
            # ใช้ filter แทน get เพื่อดึงทุกการลงทะเบียนที่ตรงกัน
            registrations_to_delete = CourseRegistration.objects.filter(user=request.user, course__course_code=course_code)
            registrations_to_delete.delete()  # ลบการลงทะเบียนทั้งหมดที่ตรงกับเงื่อนไข
        return redirect('home')  # ส่งผู้ใช้กลับไปยังหน้าหลัก

    return render(request, 'cancel_course/cancel_course.html', {'registrations': registrations})
