from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)