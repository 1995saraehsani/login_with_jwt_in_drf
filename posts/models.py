from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    title=models.CharField(max_length=250)
    body=models.TextField()
    date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title