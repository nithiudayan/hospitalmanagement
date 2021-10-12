from django.db import models

# Create your models here.
class signin(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    role=models.CharField(max_length=100)

class registration(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    mobile=models.BigIntegerField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    logid=models.ForeignKey(signin,on_delete=models.CASCADE)

