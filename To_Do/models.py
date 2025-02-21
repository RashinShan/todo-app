from django.db import models

from django_cryptography.fields import encrypt

class Task(models.Model):
    title=encrypt(models.CharField(max_length=255))
    description=encrypt(models.TextField())
    completed=models.BooleanField(default=False)


    def __str__(self):
        return self.title
