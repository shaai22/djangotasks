from django.contrib import admin

# Register your models here.

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    fields = ['title', 'completed']

admin.site.register(Task, TaskAdmin)