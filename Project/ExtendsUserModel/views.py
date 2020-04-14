from django.shortcuts import render, redirect
from ExtendsUserModel.models import User
from Communication.models import Dialog

from django.shortcuts import get_object_or_404, get_list_or_404

def friends(request):
    login_user = request.user
    friends = User.objects.filter(friends=login_user)
    req_to = User.objects.filter(friend_requests_from=login_user)
    req_from = User.objects.filter(friend_requests_to=login_user)
    
    return render(request, 'friends.html', {
    'title':'Friends', 
    'login_user':login_user,
    'friends':reversed(list(friends)) if friends else None, 
    'req_to':req_to, 
    'req_from':req_from,
    })        

def follow(request, pk):
    login_user = request.user
    work_user = get_object_or_404(User, username=pk)
    login_user.friend_requests_to.add(work_user)
    work_user.friend_requests_from.add(login_user)
    return redirect('profile', pk=pk)

def accept(request, pk, page):
    if request.method == "POST":
        login_user = request.user
        work_user = get_object_or_404(User, username=pk)
        login_user.friend_requests_from.remove(work_user)
        login_user.friends.add(work_user)
        work_user.friend_requests_to.remove(login_user)
        work_user.friends.add(login_user)

        if Dialog.objects.filter(connected_to = login_user, dialog_with = work_user) and Dialog.objects.filter(connected_to = work_user, dialog_with = login_user):
            pass
        else:
            dialog_1 = Dialog.objects.create(connected_to = login_user, dialog_with = work_user)
            dialog_2 = Dialog.objects.create(connected_to = work_user, dialog_with = login_user)
            dialog_1.save()
            dialog_2.save()

        if page == 'profile':
            return redirect('profile', pk=work_user.username)
        elif page == 'friends':
            return redirect('friends')

def unfollow(request, pk, page):
    if request.method == "POST":
        login_user = request.user
        work_user = get_object_or_404(User, username=pk)
        login_user.friend_requests_to.remove(work_user)
        work_user.friend_requests_from.remove(login_user)
        if page == 'profile':
            return redirect('profile', pk=work_user.username)
        elif page == 'friends':
            return redirect('friends')

def unfriend(request, pk, page):
    if request.method == "POST":
        login_user = request.user
        work_user = get_object_or_404(User, pk=pk)
        login_user.friends.remove(work_user)
        login_user.friend_requests_from.add(work_user)
        work_user.friends.remove(login_user)
        work_user.friend_requests_to.add(login_user)
        if page == 'profile':
            return redirect('profile', pk=work_user.username)
        elif page == 'friends':
            return redirect('friends')

def user_search(request, pk):
    login_user = request.user
    friends = User.objects.filter(friends=login_user)
    req_to = User.objects.filter(friend_requests_from=login_user)
    req_from = User.objects.filter(friend_requests_to=login_user)
    
    return render(request, 'friends.html', {
    'title':'Friends', 
    'login_user':login_user,
    'friends':reversed(list(friends)) if friends else None, 
    'req_to':req_to, 
    'req_from':req_from,
    })  