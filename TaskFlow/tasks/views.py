from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm

from comments.models import Comment
from comments.forms import CommentForm


@login_required
def create_task(request):

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = TaskForm()

    return render(
        request,
        'create_task.html',
        {
            'form': form
        }
    )


@login_required
def task_detail(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    comments = Comment.objects.filter(task=task)

    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            comment.task = task
            comment.user = request.user

            comment.save()

            return redirect(
                'task_detail',
                task_id=task.id
            )

    else:

        form = CommentForm()

    return render(
        request,
        'task_detail.html',
        {
            'task': task,
            'comments': comments,
            'form': form
        }
    )