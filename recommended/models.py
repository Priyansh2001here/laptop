from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



