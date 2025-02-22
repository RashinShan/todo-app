# In models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    completed = models.BooleanField(default=False) 

    def __str__(self):
        return self.title
