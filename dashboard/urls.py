from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="dash"),
    path('create/', views.create_task, name = "add"),
    path('display/', views.display_tasks, name='dsiplay'),
    path('update/<int:task_id>/', views.update_task, name='update'),
    path('delete/<int:task_id>/', views.delete_task, name='delete'),


]