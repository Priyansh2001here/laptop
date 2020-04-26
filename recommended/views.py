from django.shortcuts import render, redirect
from .models import Category
from django.http import HttpResponse
from best_laptops.models import Laptop
from accounts.models import Comment


# Create your views here.
def categories(request):
    categories_laptops = Category.objects.all()
    return render(request, 'recommended.html', {"categories": categories_laptops})


def show_products(request, laptop_category):
    category = Category.objects.filter(name=laptop_category)  # Query Set
    category = category[0]  # Category
    return render(request, 'products.html', {'category': category, "user": request.user})


def show_laptop(request, req_laptop, laptop_category):
    laptop = Laptop.objects.filter(laptop_name=req_laptop)
    laptop = laptop[0]
    return render(request, 'product_details.html', {"laptop_details": laptop, "user": request.user})


def add_comment(request, req_laptop):
    print("\n\n" + "fun")
    comment = request.GET['user_comment']
    print('\n\n' + comment + '\n\n')
    c1 = Comment()
    c1.user = request.user
    c1.comment = comment
    req_laptop = Laptop.objects.get(laptop_name=req_laptop)
    c1.to_which = req_laptop
    c1.save()
    return show_laptop(request, req_laptop, req_laptop.category)
