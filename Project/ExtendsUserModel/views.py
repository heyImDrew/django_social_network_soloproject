from django.shortcuts import render
from ExtendsUserModel.models import User

from django.shortcuts import get_object_or_404, get_list_or_404

def friends(request):
    info = True if (request.user.friends or request.user.friend_requests_to or request.user.friend_requests_from) else False

    return render(request, 'friends.html', {
    'title':'Friends', 
    'login_user':request.user,
    'friends':request.user.friends, 
    'friends_requests_to':request.user.friend_requests_to, 
    'friends_requests_from':request.user.friend_requests_from,
    'info':info,
    })        