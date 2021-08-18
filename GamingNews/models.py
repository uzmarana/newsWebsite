from django.db import models

# Create your models here.


class roblox(models.Model):
    postTittle = models.CharField(max_length=100, unique=False)
    post = models.CharField(max_length=10000, unique=False)


class creategame(models.Model):
    postTittle = models.CharField(max_length=100, unique=False)
    post = models.CharField(max_length=10000, unique=False)
