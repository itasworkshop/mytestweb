from django.db import models
from datetime import datetime
from django.utils import  timezone

# Create your models here.
class Department(models.Model):
    dt_id = models.IntegerField()
    dt_name = models.CharField(max_length=20)
    dt_location = models.CharField(max_length=20)

class Student(models.Model):
    st_did = models.ForeignKey(Department,on_delete=models.CASCADE)
    st_roll = models.IntegerField()
    st_name = models.CharField(max_length=20)
    st_sub = models.CharField(max_length=20)
    st_join_date = models.DateTimeField(default=timezone.now)

