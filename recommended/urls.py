from django.urls import path
from recommended import views

app_name = 'recommended'
urlpatterns = [
    path('categories/', views.categories, name="show_categories"),
    path('categories/<str:laptop_category>', views.show_products, name='show_laptops_in_category'),
    path('categories/<str:laptop_category>/<str:req_laptop>', views.show_laptop, name='req_laptop'),
    path('<str:req_laptop>/add_comment', views.add_comment, name='user_comment'),
]
