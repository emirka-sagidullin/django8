from django.db import models

# Create your models here.

class Post(models.Model):
    heading = models.CharField(max_length=20)
    url = models.URLField()
    content = models.TextField()
    publication = models.CharField(max_length=3)
    category = models.CharField(max_length=20)