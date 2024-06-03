from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def task_list(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'tasksapp/index.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('task-title')
        if not title:
             pass
        else:
            Task.objects.create(title=title)

    return redirect('task_list')

def finish_task(request, task_id):
    task = Task.objects.get(id = task_id)
    task.completed = True
    task.save()
    
    return redirect('task_list')

def delete_task(request, task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    
    return redirect('task_list')