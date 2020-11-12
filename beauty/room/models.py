from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.full_name



class Service(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)
    price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    master = models.ManyToManyField('Master',null=True)
    image = models.ImageField(null=True,blank=True,default='')

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=100,null=True)
    full_name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.full_name


class Contact(models.Model):
    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.name


class Master(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)
    image = models.ImageField(null=True,blank=True,default='')

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)
    image = models.ImageField(null=True,blank=True,default='')
    master = models.ManyToManyField(Master, null=True)

    def __str__(self):
        return self.name








