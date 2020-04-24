from django.shortcuts import render
from django.http import HttpResponse
from best_laptops.models import Laptop, Companies, NewLaptopReleases


# Create your views here.
def home(request):
    # top companies hp, lenovo, asus
    # c1 = Companies()
    # c1.company_name = "Lenovo"
    # c1.company_desc = "Lenovo is a Chinese multinational technology company with " \
    #                   "headquarters in Beijing.Lenovo is the world's largest personal computer " \
    #                   "vendor by unit sales, as of March 2019. Lenovo has operations in more than 60 countries and " \
    #                   "sells its products in around 160 countries."
    # c1.company_image = "Lenovo.jpg"
    # c2 = Companies()
    # c2.company_name = "HP"
    # c2.company_desc = "The Hewlett-Packard Company (commonly referred to as HP, and stylized as hp), " \
    #                   "or Hewlett-Packard is an American multinational " \
    #                   "information technology company headquartered in Palo Alto, California. It developed and " \
    #                   "provided a wide variety of hardware components as well as software and related services."
    # c2.company_image = "hp.jpeg"
    # c3 = Companies()
    # c3.company_desc = "susTek Computer Inc. (stylised as ASUSTeK or ASUS) is a Taiwan-based multinational computer " \
    #                   "and phone hardware and electronics company headquartered in Beitou District, Taipei, " \
    #                   "Taiwan. Its products include desktop computers, laptops, netbooks, mobile phones, networking " \
    #                   "equipment, monitors, WIFI routers, projectors, motherboards, graphics cards, optical storage, " \
    #                   "multimedia products, peripherals, wearables, servers, workstations, and tablet PCs. The " \
    #                   "company is also an original equipment manufacturer (OEM).Asus is the worlds 5th-largest PC " \
    #                   "vendor by 2017 unit sales "
    # c3.company_image = "asus-rog.jpg"
    companies = Companies.objects.all()
    new_laptops = NewLaptopReleases.objects.all()
    return render(request, "index.html", {"companies": companies, "new_laptops": new_laptops})
