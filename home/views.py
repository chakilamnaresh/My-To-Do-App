from django.shortcuts import render
from dashboard.models import Tasks

def home(request):
    completed_tasks = Tasks.objects.filter(status='completed').count()
    pending_tasks = Tasks.objects.filter(status='pending').count()
    hold_tasks = Tasks.objects.filter(status='hold').count()
    return render(request, './home/home.html', {'completed_tasks': completed_tasks, 'pending_tasks': pending_tasks, 'hold_tasks': hold_tasks})
    
