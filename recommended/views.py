from django.shortcuts import render
from .models import Category
from django.http import HttpResponse
from best_laptops.models import Laptop


# Create your views here.
def categories(request):
    categories_laptops = Category.objects.all()
    return render(request, 'recommended.html', {"categories": categories_laptops})


def show_products(request, laptop_category):
    category = Category.objects.filter(name=laptop_category)  # Query Set
    category = category[0]  # Category
    return render(request, 'products.html', {'category': category})


def show_laptop(request, req_laptop, laptop_category):
    laptop = Laptop.objects.filter(laptop_name=req_laptop)
    laptop = laptop[0]
    return render(request, 'product_details.html', {"laptop_details": laptop})
