from django.shortcuts import render , redirect
from courses.models import Course
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, CourseRegistration


def course_list(request):
    courses = Course.objects.all()  # ดึงข้อมูลวิชาทั้งหมด
    return render(request, 'course_selection/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course_selection/course_detail.html', {'course': course})

def course_selection_home(request):
    # ดึงข้อมูลวิชาทั้งหมดที่เปิดให้ลงทะเบียนได้
    available_courses = Course.objects.filter(enrollment_status=True)
    
    if request.method == 'POST':
        selected_course_id = request.POST.get('course_id')
        if selected_course_id:
            selected_course = Course.objects.get(id=selected_course_id)
            # เพิ่มการบันทึกการลงทะเบียน
            registration_complete.objects.create(user=request.user, course=selected_course)
            return redirect('register_subject_complete')  # พาผู้ใช้ไปยังหน้าลงทะเบียนเสร็จสิ้น
        
    context = {
        'courses': available_courses
    }
    
    return render(request, 'course_selection/course_selection_home.html', context)

def course_register(request,course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        registration = CourseRegistration(user=request.user, course=course)
        registration.save()  # ตรวจสอบให้แน่ใจว่าบันทึกข้อมูลอย่างถูกต้อง
        return redirect('register_complete')  # เปลี่ยนเส้นทางไปยังหน้าสำเร็จ
    return render(request, 'course_selection/register.html', {'course': course})
    
def registration_complete(request):
    return render(request, 'course_selection/register_subject_complete.html')