from django.shortcuts import render
from .models import Project
from django.shortcuts import render, redirect
from .forms import ProjectForm
from tasks.models import Task

def home(request):

    projects = Project.objects.all()

    todo_tasks = Task.objects.filter(status='To Do')
    progress_tasks = Task.objects.filter(status='In Progress')
    completed_tasks = Task.objects.filter(status='Completed')

    return render(
        request,
        'home.html',
        {
            'projects': projects,
            'todo_tasks': todo_tasks,
            'progress_tasks': progress_tasks,
            'completed_tasks': completed_tasks,
        }
    )

def create_project(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ProjectForm()

    return render(
        request,
        'create_project.html',
        {'form': form}
    )