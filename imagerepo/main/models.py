from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_title = models.CharField(max_length=100)
    image_desc = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return f'Title: {self.image_title}\nDesc: {self.image_desc}\nURL: {self.image.url}'