from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    title  = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('TODO', 'To Do'), ('IN_PROGRESS', 'In Progess'), ('DONE', 'Done')])
    deadline = models.DateTimeField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)


