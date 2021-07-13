from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ExamSubject)
admin.site.register(Question)
#admin.site.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student','exam','marks','date','status')

admin.site.register(Result,ResultAdmin)