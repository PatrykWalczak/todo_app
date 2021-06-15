from django.shortcuts import render
from django.views.generic.list import ListView
from .models import TaskModels


class TaskListView(ListView):
    model = TaskModels
    context_object_name = 'tasksmodel'