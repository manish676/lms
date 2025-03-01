from django.db import models

class Status(models.Model):
    title = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    createdAt = models.DateTimeField(auto_now_add=True)