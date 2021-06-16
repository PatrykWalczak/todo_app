from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import TaskModels


class TaskListView(ListView):
    model = TaskModels
    context_object_name = 'tasklist'
    template_name = 'base_app/task_list.html'


class TaskDetailView(DetailView):
    model = TaskModels
    context_object_name = 'taskdetail'
    template_name = 'base_app/task.html'  # gdy chcemy zmienić nazwe templatki na taką jaka nam się podoba


class TaskCreateView(CreateView):
    model = TaskModels
    template_name = 'base_app/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):  # wykorzystano do update ten same html file list
    model = TaskModels
    template_name = 'base_app/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class DeleteView(DeleteView):
    model = TaskModels
    template_name = 'base_app/task_confirm_delete.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')







