from django.urls import path
from .views import cancel_course_registration

urlpatterns = [
    path('', cancel_course_registration, name='cancel_course'),  # เปลี่ยนเป็น '/' เพื่อให้สามารถเข้าถึงได้ที่ '/cancel_course/'
]
