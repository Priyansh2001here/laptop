from django.contrib import admin
from best_laptops.models import Laptop, Companies, NewLaptopReleases

# Register your models here.
admin.site.register(Companies)
admin.site.register(NewLaptopReleases)
admin.site.register(Laptop)

