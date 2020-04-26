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
    path('friend/remove/<str:which_user>', views.remove, name='remove'),
    path('message/show', views.show_msg_friends, name='show_frnd_for_msg'),
    path('message/<str:user_name>', views.message_to, name='mesageUser'),
    path('message/<str:to_user>/send', views.send_msg, name='sendMsg'),
    path('message/<str:from_user>/view_message', views.show_messages, name='seemessages')
]
