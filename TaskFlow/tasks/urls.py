from django.urls import path
from .views import create_task, task_detail

urlpatterns = [
    path('create-task/', create_task, name='create_task'),

    path(
        'task/<int:task_id>/',
        task_detail,
        name='task_detail'
    ),
]