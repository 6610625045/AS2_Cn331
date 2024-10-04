# login-logout/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

# ฟังก์ชันสำหรับหน้าหลัก
  # ใช้เพื่อให้แน่ใจว่าผู้ใช้จะต้องล็อกอินก่อนถึงจะเข้าได้
@login_required
def home(request):
    return render(request, 'login-logout/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # เปลี่ยนเส้นทางไปยังหน้าหลักหลังล็อกอิน
    else:
        form = AuthenticationForm()
    return render(request, 'login-logout/login.html', {'form': form})

def logout_view(request):
    logout(request)  # ล็อกเอาต์ผู้ใช้
    return redirect('login')  # เปลี่ยนเส้นทางไปยังหน้าล็อกอินหลังล็อกเอาต์