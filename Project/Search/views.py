from django.shortcuts import render, redirect
from .forms import SearchForm
from ExtendsUserModel.models import User

from django.shortcuts import get_object_or_404, get_list_or_404

def search(request):
    if request.method=='GET':
        login_user = request.user
        query = request.GET.get('q')
        result = User.objects.filter(username=query)
        if result:
            person=result.get()
        else:
            person=None
        return render(request, 'search.html', {
            'login_user':login_user,
            'title':'Search results',
            'query':query,
            'person':person,
        })