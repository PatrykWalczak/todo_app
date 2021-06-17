from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import TaskModels


class TaskLoginView(LoginView):
    template_name = 'base_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskRegisterView(FormView):
    template_name = 'base_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(TaskRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(TaskRegisterView, self).get(*args, **kwargs)


class TaskListView(LoginRequiredMixin, ListView):  # dodanie LoginMixin powoduje, że niezalogowanemu uzytkownikowi
    # nie pojawi się strona dostępu a zostanie przekierowany na strone logowania.
    model = TaskModels
    context_object_name = 'tasks'
    template_name = 'base_app/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = TaskModels
    context_object_name = 'taskdetail'
    template_name = 'base_app/task.html'  # gdy chcemy zmienić nazwe templatki na taką jaka nam się podoba


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = TaskModels
    template_name = 'base_app/task_form.html'
    fields = {'title', 'description', 'complete'}
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):  # wykorzystano do update ten same html file list
    model = TaskModels
    template_name = 'base_app/task_form.html'
    fields = {'title', 'description', 'complete'}
    success_url = reverse_lazy('tasks')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskModels
    template_name = 'base_app/task_confirm_delete.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')







