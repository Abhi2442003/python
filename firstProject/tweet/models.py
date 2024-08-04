from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Tweet (models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    photo= models.ImageField(upload_to='tweet/', blank=True , null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return f'{self.user.username}-{self.text[0:10]}'

 