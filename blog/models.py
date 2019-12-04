from django.db import models

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to ='media/')
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=10000)
    pubdate = models.DateField(auto_now_add=True)
