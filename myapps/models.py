from django.db import models

# Create your models here.
class Details(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=254,unique=True)
    password = models.CharField(max_length=50)
    gender=models.CharField(max_length=70)

    def __str__(self):
        return self.username