from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from friendship.models import Friend, Follow, Block
from django.http import HttpResponse
from friendship.models import FriendshipRequest


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
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                password=password1, username=username)
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
        print("\n\n" + username + "," + password + "\n\n")
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


def show_friend(request, operation):
    if operation == 'show':
        friends = Friend.objects.friends(request.user)
        unread_friend_requests = Friend.objects.unread_requests(user=request.user)
        return render(request, 'show_friends.html',
                      {"friends": friends, "unread_friend_requests": unread_friend_requests})
    if operation == 'requests':
        requests = FriendshipRequest.objects.filter(to_user=request.user)
        requests = [i.from_user for i in requests]
        return render(request, "requests.html", {"requests": requests})


def friend_opt(request):
    return render(request, "friend_opt.html")


def add_page(request):
    users = User.objects.all()
    return render(request, "add_friend.html", {"users": users})


def add(request, to_user):
    other_user = User.objects.get(username=to_user)
    Friend.objects.add_friend(from_user=request.user, to_user=other_user, message="I want to be friend with you")
    return HttpResponse("Friend Request has been sent")


def accept(request, req_from):
    user = User.objects.get(username=req_from)
    print(user)
    friend_requests = FriendshipRequest.objects.filter(from_user=user)
    print(friend_requests)
    friend_requests[0].accept()
    return show_friend(request, operation="requests")


def remove(request, which_user):
    user = User.objects.get(username=which_user)
    Friend.objects.remove_friend(request.user, user)
    return show_friend(request, operation="show")
