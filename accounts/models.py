from best_laptops.models import Laptop
from django.db import models
from django.contrib.auth.models import auth, User


# Create your models here.
class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    to_which = models.ForeignKey(Laptop, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Message(models.Model):
    msg = models.TextField(default=1)
    from_user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    unread = models.BooleanField(default=True)

    def __str__(self):
        return self.msg


class Msgfromuser(models.Model):
    to_user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    msg = models.ForeignKey(Message, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.msg.from_user)
