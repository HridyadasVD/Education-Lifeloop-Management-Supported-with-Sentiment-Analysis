from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name = "index"),
    path('register/',views.register,name = 'register'),
    path('user_login/',views.user_login, name = 'user_login'),
    path('user_logout/',views.user_logout, name = 'user_logout'),
    path('student-exam', views.student_exam_view,name='student-exam'),
    path('take-exam/<int:pk>', views.take_exam_view,name='take-exam'),
    path('start-exam/<int:pk>', views.start_exam_view,name='start-exam'),
    path('calculate-marks', views.calculate_marks_view,name='calculate-marks'),
    path('view-result', views.view_result_view,name='view-result'),
    path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),
    path('student-marks', views.student_marks_view,name='student-marks'),
    path('contact/',views.contact,name='contact'),
    path('all_mark',views.all_mark,name='all_mark'),
    path('review', views.review, name='review'),
    path('view_review', views.view_review, name='view_review'),

   
   
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
