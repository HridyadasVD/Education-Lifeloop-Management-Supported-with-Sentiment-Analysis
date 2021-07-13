from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
import os
from django.urls import reverse



# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(null=True,blank=True)
    description = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)


def save_subject_image(instance,filename):
    upload_to = "Images/"
    ext = filename.split('.')[-1]
    if instance.subject_id:
        filename = 'Subject_pictures/{}.{}'.format(instance.subject_id,ext)
    return os.path.join(upload_to,filename)

class Subject(models.Model):
    subject_id = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True,blank=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='subjects')
    image = models.ImageField(upload_to = save_subject_image, blank = True, verbose_name = 'subject image' )
    description = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject_id)
        super().save(*args, **kwargs)





def save_lesson_files(instance,filename):
    upload_to = "File_Folder/"
    ext = filename.split('.')[-1]
    if instance.lesson_id:
        filename = 'Lesson_Files/{}/{}.{}'.format(instance.lesson_id,instance.lesson_id,ext)
        if os.path.exists(filename):
            new_name = str(instance.lesson_id) + str('1')
            filename = 'Lesson_Files/{}/{}.{}'.format(instance.lesson_id,new_name,ext)
    return os.path.join(upload_to,filename)

class Lesson(models.Model):
    lesson_id = models.CharField(max_length=100,unique=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='lessons')
    name = models.CharField(max_length=100)
    position = models.PositiveSmallIntegerField(verbose_name='Chapter no.')
    slug = models.SlugField(null=True,blank=True)
    video = models.FileField(upload_to=save_lesson_files,verbose_name='Video',blank=True,null=True)
    ppt = models.FileField(upload_to=save_lesson_files,verbose_name='Presentation',blank=True)
    notes = models.FileField(upload_to=save_lesson_files,verbose_name='Notes',blank=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('cariculam:lesson_list', kwargs={'slug':self.subject.slug, 'course':self.course.slug})

class Comment(models.Model):
    lesson_name = models.ForeignKey(Lesson,null=True, on_delete=models.CASCADE,related_name='comments')
    comm_name = models.CharField(max_length=100, blank=True)
    # reply = models.ForeignKey("Comment", null=True, blank=True, on_delete=models.CASCADE,related_name='replies')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.comm_name = slugify("comment by" + "-" + str(self.author) + str(self.date_added))
        super().save(*args, **kwargs)

    def _str_(self):
        return self.comm_name

    class Meta:
        ordering = ['-date_added']

class Reply(models.Model):
    comment_name = models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='replies')
    reply_body = models.TextField(max_length=500)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return "reply to " + str(self.comment_name.comm_name)