from django.shortcuts import render
from django.urls import reverse_lazy
from tasks.models import Task
from tasks.forms import TaskForm
from django.views.generic import ListView, DetailView, CreateView


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"
    
    
class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "tasks/task_detail.html"
    

class TaskCreateView(CreateView):
    model = Task
    template_name = "tasks/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-list")
    