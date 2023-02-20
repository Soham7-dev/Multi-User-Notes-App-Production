from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    body = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body[0:50]
