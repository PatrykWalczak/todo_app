from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdate, DeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='single-task'),
    path('create-task/', TaskCreateView.as_view(), name='task-create'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', DeleteView.as_view(), name='delete-task'),
]
