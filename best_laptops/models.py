from django.db import models
from recommended.models import Category
from ckeditor.fields import RichTextField


# Create your models here.
class Companies(models.Model):
    company_image = models.ImageField()
    company_name = models.CharField(max_length=10)
    company_desc = RichTextField()
    best_company = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name


class Laptop(models.Model):
    laptop_name = models.CharField(max_length=50)
    laptop_serial = models.CharField(max_length=30)
    cost = models.IntegerField()
    laptop_image = models.ImageField(null=True)
    laptop_link_1 = models.URLField(null=True)
    laptop_link_2 = models.URLField(null=True)
    category = models.ManyToManyField(Category)
    company = models.ForeignKey(Companies, default=0, on_delete=models.CASCADE)
    NewlyLaunched = models.BooleanField(default=False)

    def __str__(self):
        return self.laptop_name


class NewLaptopReleases(models.Model):
    laptop_name = models.CharField(max_length=50)
    laptop_desc = models.CharField(max_length=200)
    laptop_img = models.ImageField()
    laptop_default_link = models.URLField()
