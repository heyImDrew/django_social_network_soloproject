from django.shortcuts import render
from ExtendsUserModel.models import User
from Thoughts.models import Post
from .forms import PostForm

from django.shortcuts import get_object_or_404, get_list_or_404

def show_users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'title':'Users', 'users':users})

def profile(request, pk):
    login_user = request.user
    now_at_user = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(connected_to = now_at_user)
    title = now_at_user.first_name + ' ' + now_at_user.last_name if (now_at_user.first_name and now_at_user.last_name) else 'Profile'
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = Post(
                connected_to = request.user,
                text = form.cleaned_data.get('text')
            )
            new_post.save()
            posts = Post.objects.filter(connected_to = now_at_user)
    
    return render(request, 'profile.html', {'title':title, 'login_user':login_user, 'now_at_user':now_at_user, 'posts':posts})        