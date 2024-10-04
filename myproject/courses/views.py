from django.shortcuts import render
from django.shortcuts import render, redirect
from courses.models import Course

def course_list(request):
    # คุณสามารถดึงข้อมูลวิชาจากฐานข้อมูลที่นี่
    return render(request, 'courses/course_list.html')

def course_selection_home(request):
    courses = Course.objects.filter(enrollment_status=True)

    if request.method == 'POST':
        selected_courses = request.POST.getlist('courses')
        # ทำการลงทะเบียนวิชาในที่นี้ เช่น บันทึกลงในโมเดลใหม่
        # หรือดำเนินการที่คุณต้องการเมื่อผู้ใช้ลงทะเบียน

        # ตัวอย่าง: แสดงผลลัพธ์การลงทะเบียน
        return redirect('home')  # เปลี่ยนเส้นทางไปยังหน้า home หรือหน้าที่คุณต้องการหลังการลงทะเบียน

    return render(request, 'course_selection/course_selection_home.html', {'courses': courses})