from django.shortcuts import render
from Communication.models import Message

from django.shortcuts import get_object_or_404, get_list_or_404

def messages(request):
    return render(request, 'messages.html', {
    'title':'Messages', 
    'login_user':request.user,
    })