from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('friend/', views.friend_opt, name='frient_opt'),
    path('friend/<str:operation>', views.show_friend, name='friend'),
    path('add', views.add_page, name='add_page'),
    path('add/<str:to_user>', views.add, name='add_friend'),
    path('<str:req_from>', views.accept, name='accept'),
    path('friend/remove/<str:which_user>', views.remove, name='remove')
]
