from django.shortcuts import render
from .models import User

def show_users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'title':'Users', 'users':users})

def profile(request, pk):
    login_user = request.user
    now_at_user = User.objects.get(pk=pk)
    title = now_at_user.first_name + ' ' + now_at_user.last_name
    return render(request, 'profile.html', {'title':title, 'login_user':login_user, 'now_at_user':now_at_user})
