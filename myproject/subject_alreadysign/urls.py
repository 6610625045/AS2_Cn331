from django.urls import path
from . import views


urlpatterns = [
    path('registered-courses/', views.registered_courses, name='registered_courses'),
]
