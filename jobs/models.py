from django.db import models

class Job(models.Model):
    image=models.ImageField(upload_to='images/')
    text=models.CharField(max_length=200)
