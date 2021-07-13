"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from exam import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls')),
    path('cariculam/',include('cariculam.urls')),
    path('exam/',include('exam.urls')),

    path('delete_subject/<int:pk>/', views.delete_subject,name='delete_subject'),
    path('view_question/<int:pk>/',views.view_question,name="view_question"),
    path('delete_view/<int:pk>/',views.delete_question,name='delete_view'),

 
  
]
