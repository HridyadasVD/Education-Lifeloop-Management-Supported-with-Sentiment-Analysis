from django.urls import path
from .import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


app_name = 'cariculam'
urlpatterns = [
    path('',views.CourseListView.as_view(),name = 'course_list'),
    path('<slug:slug>/',views.SubjectListView.as_view(),name = 'subject_list'),
   
    path('<str:course>/<slug:slug>/', views.LessonListView.as_view(), name='lesson_list'),
    path('<str:course>/<str:slug>/create/',views.LessonCreateView.as_view(),name= 'lesson_create'),
    path('<str:course>/<str:subject>/<slug:slug>/',views.LessonDetailView.as_view(),name = 'lesson_detail'),
    path('<str:course>/<str:subject>/<slug:slug>/update/', views.LessonUpdateView.as_view(),name='lesson_update'),
    path('<str:course>/<str:subject>/<slug:slug>/delete/', views.LessonDeleteView.as_view(),name='lesson_delete'),
    
    
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
