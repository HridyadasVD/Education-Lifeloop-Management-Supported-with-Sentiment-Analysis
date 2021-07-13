from django.urls import path
from .import views


app_name = 'exam'
urlpatterns = [
    path('',views.subject,name='subject'),
    path('exam_subject/',views.exam_subject,name='exam_subject'),
    path('add_subject/',views.add_subject,name='add_subject'),
    path('question/', views.question,name='question'),
    path('add_question_view/', views.add_question_view,name='add_question_view'),
    path('question_view/', views.question_view,name='question_view'),
   


]