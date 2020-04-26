from django.contrib import admin
from .models import Comment, Msgfromuser, Message

admin.site.register(Comment)
admin.site.register(Msgfromuser)
admin.site.register(Message)