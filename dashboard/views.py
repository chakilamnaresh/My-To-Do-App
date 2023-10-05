from django.shortcuts import render,redirect,get_object_or_404
from . models import Tasks
from django.contrib.auth.models import User


# Create your views here.

def dashboard(request):
    return render(request, './dashboard/dashboard.html')


def create_task(request):
    if request.method == 'POST':
        created_by = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        task = Tasks(title=title, description=description, priority=priority, status=status, created_by = created_by)
        if task:
            task.save()
            print("task saved")
            return redirect('home')
        else:
            return render(request, './dashboard/add_task.html')
    return render(request, './dashboard/add_task.html')


def display_tasks(request):
    if request.user.is_authenticated:
        tasks = Tasks.objects.filter(created_by=request.user)
        print(tasks)
        return render(request, './dashboard/display.html',{'tasks': tasks})

def update_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.priority = request.POST.get('priority')
        task.status = request.POST.get('status')
        task.save()
        return redirect('home')
    return render(request, './dashboard/update.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, './dashboard/delete.html', {'task': task})