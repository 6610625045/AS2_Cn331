from django.urls import path
from .views import course_list, course_detail
from . import views

urlpatterns = [
    path('', course_list, name='course_list'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('course-selection/', views.course_selection_home, name='course_selection_home'),
]
