from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)
    price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=100,null=True)
    full_name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.full_name


class Contacts(models.Model):
    name = models.CharField(max_length=100,null=True)
    full_name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)


    def __str__(self):
        return self.full_name


class Masters(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name








