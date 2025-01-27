from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
