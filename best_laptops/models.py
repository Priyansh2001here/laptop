from django.db import models
from recommended.models import Category


# Create your models here.
class Laptop(models.Model):
    laptop_name = models.CharField(max_length=50)
    company = models.CharField(max_length=10)
    laptop_serial = models.CharField(max_length=30)
    cost = models.IntegerField()
    laptop_image = models.ImageField(null=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.laptop_name


class Companies(models.Model):
    company_image = models.ImageField()
    company_name = models.CharField(max_length=10)
    company_desc = models.CharField(max_length=200)


class NewLaptopReleases(models.Model):
    laptop_name = models.CharField(max_length=50)
    laptop_desc = models.CharField(max_length=200)
    laptop_img = models.ImageField()
    laptop_default_link = models.URLField()
