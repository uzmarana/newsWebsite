from django.db import models

# Create your models here.


class Newfood(models.Model):
    postTittle = models.CharField(max_length=100, unique=False)
    post = models.CharField(max_length=10000, unique=False)


class createpost(models.Model):
    postTittle = models.CharField(max_length=100, unique=False)
    post = models.CharField(max_length=10000, unique=False)
