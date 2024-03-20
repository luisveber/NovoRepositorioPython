from django.shortcuts import render
from .models import Task
from django.http import JsonResponse

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'myapp/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return JsonResponse({'message': 'Task created successfully!'})
