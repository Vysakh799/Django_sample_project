from django.db import models

# Create your models here.
class student(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=20)
    age=models.IntegerField()

    def __str__(self):
        return self.name

class uploads(models.Model):
    dis=models.TextField()
    file=models.FileField()
    
