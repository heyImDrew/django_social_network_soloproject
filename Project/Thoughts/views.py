from django.shortcuts import render
from ExtendsUserModel.models import User
from Thoughts.models import Post, Comment
from .forms import PostForm

from django.shortcuts import get_object_or_404, get_list_or_404

def profile(request, pk):
    posts = Post.objects.filter(connected_to = get_object_or_404(User, pk=pk))
    comments = Comment.objects.filter(connected_person_to_post = get_object_or_404(User, pk=pk))
    friends = [fr for fr in User.objects.all() if fr in request.user.friends.all()]
    req_to = [req for req in User.objects.all() if req in request.user.friend_requests_to.all()]
    req_from = [req for req in User.objects.all() if req in request.user.friend_requests_from.all()]

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = Post(
                connected_to = request.user,
                text = form.cleaned_data.get('text')
            )
            new_post.save()
            posts = Post.objects.filter(connected_to = get_object_or_404(User, pk=pk))
            
    return render(request, 'profile.html', {
        'title':get_object_or_404(User, pk=pk).first_name + ' ' + get_object_or_404(User, pk=pk).last_name + ' (' + get_object_or_404(User, pk=pk).username + ')' if (get_object_or_404(User, pk=pk).first_name and get_object_or_404(User, pk=pk).last_name) else 'Profile', 
        'login_user':request.user, 
        'now_at_user':get_object_or_404(User, pk=pk), 
        'posts':posts, 
        'comments':comments,
        'friends':friends,
        'req_to':req_to,
        'req_from':req_from,
        })        