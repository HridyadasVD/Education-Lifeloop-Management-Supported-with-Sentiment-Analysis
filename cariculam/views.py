#from django.db import models
from django.shortcuts import render
from django.views.generic import (DetailView, ListView, FormView, CreateView, UpdateView, DeleteView)
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# Create your views here.

class CourseListView(ListView):
    context_object_name = 'courses'
    model = Course
    template_name = 'course_list_view.html'



class SubjectListView(DetailView):
    context_object_name = 'courses'
    model = Course
    template_name = 'subject_list_view.html'

# Create your views here.


class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'lesson_list_view.html'


class LessonDetailView(DetailView, FormView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'lesson_detail_view.html'
    form_class = CommentForm
    second_form_class = ReplyForm

    # Feedback Section
    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(request=self.request)
        if 'form2' not in context:
            #context['form2'] = self.second_form_class(request=self.request)
            context['form2'] = self.second_form_class
        # context['comments'] = Comment.objects.filter(id=self.object.id)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.form_class
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'

        form = self.get_form(form_class)
        # print("the form name is : ", form)
        # print("form name: ", form_name)
        # print("form_class:",form_class)

        if form_name == 'form' and form.is_valid():
            print("comment form is returned")
            return self.form_valid(form)
        elif form_name == 'form2' and form.is_valid():
            print("reply form is returned")
            return self.form2_valid(form)

    def get_success_url(self):
        self.object = self.get_object()
        course = self.object.course
        subject = self.object.subject
        return reverse_lazy('cariculam:lesson_detail', kwargs={'course': course.slug,
                                                               'subject': subject.slug,
                                                               'slug': self.object.slug})

    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.lesson_name = self.object.comments.name
        fm.lesson_name_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form2_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.comment_name_id = self.request.POST.get('comment.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class LessonCreateView(CreateView):
    form_class = Lessonform
    context_object_name = 'subject'
    model = Subject
    template_name = 'lesson_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        course = self.object.course
        return reverse_lazy('cariculam:lesson_list', kwargs={'course': course.slug, 'slug': self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.course = self.object.course
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class LessonUpdateView(UpdateView):
    fields = ('name', 'position', 'video', 'ppt', 'notes')
    model = Lesson
    template_name = 'lesson_update.html'
    context_object_name = 'lessons'


class LessonDeleteView(DeleteView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'lesson_delete.html'

    def get_success_url(self):
        print(self.object)
        course = self.object.course
        subject = self.object.subject
        return reverse_lazy('cariculam:lesson_list', kwargs={'course': course.slug, 'slug': subject.slug})