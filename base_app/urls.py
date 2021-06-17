from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdate, TaskDeleteView, TaskLoginView, TaskRegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', TaskLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', TaskRegisterView.as_view(), name='register'),
    path('', TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='single-task'),
    path('create-task/', TaskCreateView.as_view(), name='task-create'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', TaskDeleteView.as_view(), name='delete-task'),

]
