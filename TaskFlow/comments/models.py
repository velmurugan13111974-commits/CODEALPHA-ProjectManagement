from django.db import models
from tasks.models import Task
from django.contrib.auth.models import User

class Comment(models.Model):

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    text = models.TextField()

    def __str__(self):
        return self.text[:20]