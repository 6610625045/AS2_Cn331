# account/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # แยกกลุ่มผู้ใช้ธรรมดา
            user_group = Group.objects.get(name='User')  # สมมติว่ามีกลุ่ม 'User' ในระบบ
            user.groups.add(user_group)
            login(request, user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})
