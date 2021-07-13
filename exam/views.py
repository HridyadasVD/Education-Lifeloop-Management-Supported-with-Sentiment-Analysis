from django.http.response import HttpResponse
from django.shortcuts import render
from . import forms,models
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def subject(request):
    return render(request,'subject.html')


def add_subject(request):
    courseForm=forms.CourseForm()
    if request.method=='POST':
        courseForm=forms.CourseForm(request.POST)
        if courseForm.is_valid():        
            courseForm.save()
            return render(request,'exam_subject.html',{'msg1':'succesfully added'})
        else:
            print("form is invalid")
        return HttpResponseRedirect('/exam_subject')
    return render(request,'add_subject.html',{'courseForm':courseForm})

def exam_subject(request):
    subjects = models.ExamSubject.objects.all()
    return render(request,'exam_subject.html',{'subjects':subjects})


def delete_subject(request,pk):
    course=models.ExamSubject.objects.get(id=pk)
    course.delete()
    return render(request,'subject.html')


def question(request):
    return render(request,'question.html')

def add_question_view(request):
    questionForm=forms.QuestionForm()
    if request.method=='POST':
        questionForm=forms.QuestionForm(request.POST)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=models.ExamSubject.objects.get(id=request.POST.get('courseID'))
            question.course=course
            question.save()       
            return render(request,'question.html',{'msg1':'succesfully added'})
        else:
            print("form is invalid")
        return HttpResponseRedirect('/add_question_view')
    return render(request,'add_question_view.html',{'questionForm':questionForm})


def question_view(request):
    subjects= models.ExamSubject.objects.all()
    return render(request,'question_view.html',{'subjects':subjects})



def view_question(request,pk):
    questions=models.Question.objects.all().filter(course_id=pk)
    return render(request,'view_question.html',{'questions':questions})


def delete_question(request,pk):
    question=models.Question.objects.get(id=pk)
    question.delete()
    return render(request,'question.html')



