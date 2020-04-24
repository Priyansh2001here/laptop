from django.urls import path
from best_laptops import views

urlpatterns = [
    path('', views.home, name='home'),
]