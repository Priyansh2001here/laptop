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