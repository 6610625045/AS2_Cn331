from django.shortcuts import render
from .models import SubjectRegistration
from django.shortcuts import render
from course_selection.models import CourseRegistration  # หรือชื่อโมเดลที่ใช้สำหรับการลงทะเบียน
from django.contrib.auth.decorators import login_required

def registered_courses(request):
    if request.user.is_authenticated:
        # ดึงข้อมูลรายวิชาที่ผู้ใช้ลงทะเบียนไว้
        registrations = CourseRegistration.objects.filter(user=request.user)
        context = {
            'registrations': registrations
        }
        return render(request, 'subject_alreadysign/subject_sign.html', context)
    else:
        return render(request, 'login.html')  # เปลี่ยนเส้นทางถ้าผู้ใช้ไม่ได้ล็อกอิน
    

