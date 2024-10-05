from django.urls import path
from .views import course_list, course_detail
from . import views

urlpatterns = [
    path('', course_list, name='course_list'),
    path('course/', course_detail, name='course_detail'),
    path('course-selection/', views.course_selection_home, name='course_selection_home'),
    path('register/<str:course_code>/', views.course_register, name='course_register'),
    path('registration_complete/', views.registration_complete, name='registration_complete'),
]
