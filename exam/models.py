from django.db import models
from account.models import User_Profile
from cariculam.models import Subject


# Create your models here.
class ExamSubject(models.Model):
   subject_name = models.ForeignKey(Subject,on_delete=models.CASCADE)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()

   def __str__(self):
        return str(self.subject_name)
   

class Question(models.Model):
    course=models.ForeignKey(ExamSubject,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

    def __str__(self):
        return str(self.course)

class Result(models.Model):
    student = models.ForeignKey(User_Profile,on_delete=models.CASCADE)
    exam = models.ForeignKey(ExamSubject,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=100)

    def __str__(self):
        return str(self.student)
