from django.db import models

# Create your models here.
class results(models.Model):
    title=models.CharField(max_length=100)
    answer=models.TextField()

class languages(models.Model):
    language=models.CharField(max_length=20)
    key=models.CharField(max_length=5)    