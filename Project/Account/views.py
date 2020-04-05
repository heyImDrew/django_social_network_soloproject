from django.shortcuts import render, redirect
from ExtendsUserModel.models import User
from django.contrib import auth

def login(request):
    if request.user.is_authenticated:
        return redirect('my_profile_redirect')
 
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
 
        if user is not None:
            auth.login(request, user)
            return redirect('profile', username)
        else:
            return redirect('login')
 
    return render(request, 'registration/login.html')


def registration(request):
    if request.user.is_authenticated:
        return redirect('my_profile_redirect')

    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        if username and password and first_name and last_name:
            if not User.objects.get(username=username):
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
            else: 
                 return render(request, 'registration/registration.html', {'error':'Username is already taken!'},)
        else:
            return render(request, 'registration/registration.html', {'error':'Fill all fields first!'},)

    return render(request, 'registration/registration.html')