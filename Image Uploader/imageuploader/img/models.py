from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/')