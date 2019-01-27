from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user =  models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    done_by = models.ForeignKey(User, null=True, related_name='done_by', on_delete=models.SET_NULL)
