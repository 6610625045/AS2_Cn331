"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login_logout.urls')),
    path('account/', include('account.urls')),
    path('course_selection/', include('course_selection.urls')),
    path('courses/', include('courses.urls', namespace='courses')),  
    path('subject_alreadysign/', include('subject_alreadysign.urls')),
    path('cancel_course/', include('cancel_course.urls')),  # รวม URL ของแอป cancel_course
]
