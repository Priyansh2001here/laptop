from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['pswd1']
        password2 = request.POST['pswd2']
        print("\n--- user ---," + first_name + "\n")
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "An User With This Username already exists!!!")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, "An User With This email is already registered!!!")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password1, username=username)
                user.save()
                print("\n--- User Created ---\n")
        else:
            messages.info(request, "Passwords Donot match")

        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("\n\n"+username + "," + password+"\n\n")
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request, "Invalid Credentials !!")
            return redirect(login(request))
        else:
            auth.login(request, user)
            return redirect('/')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
