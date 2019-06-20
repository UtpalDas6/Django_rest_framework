
from django.db import models

class Author(models.Model):
  def __str__(self):
    return self.name
  name = models.CharField(max_length=255)
  email = models.EmailField()

class Article(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='articles',on_delete=models.CASCADE)