from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):

    s_name = models.CharField(max_length=20)
    c_name = models.CharField(max_length=30)
    specialisation = models.CharField(max_length=20)
    degree = models.CharField(max_length=15)
    intern = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=5)
    notes = models.CharField(max_length=50)

    def __str__(self):
        return self.s_name




