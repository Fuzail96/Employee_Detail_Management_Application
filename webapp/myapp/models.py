from django.db import models


class Employee(models.Model):
    empid=models.CharField(max_length=20)
    fName=models.CharField(max_length=40)
    lName=models.CharField(max_length=40)
    email=models.EmailField()
    contact=models.CharField(max_length=40)



