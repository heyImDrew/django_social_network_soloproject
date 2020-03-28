from django.shortcuts import render
from Communication.models import Message, Dialog
from ExtendsUserModel.models import User
from .forms import MessageForm

from django.shortcuts import get_object_or_404, get_list_or_404

def messages(request):
    login_user = request.user
    dialogs = Dialog.objects.filter(connected_to = request.user)

    return render(request, 'messages.html', {
    'title':'Messages', 
    'dialogs':reversed(list(dialogs)),
    'login_user':login_user,
    })

def dialog(request, pk):
    login_user = request.user
    dialog_with = get_object_or_404(User, id=pk)
    dialog = get_object_or_404(Dialog, connected_to = login_user, dialog_with = dialog_with)
    dialog_2 = get_object_or_404(Dialog, connected_to = dialog_with, dialog_with = login_user)
    messages = list(dialog.messages.all())

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_msg = Message(
                message_from = login_user,
                message_to = dialog_with,
                text = form.cleaned_data.get('text')
            )     
            new_msg.save()
            messages.append(new_msg)
            dialog.messages.add(new_msg)
            dialog_2.messages.add(new_msg)

    return render(request, 'dialog.html', {
    'title':'Dialog', 
    'dialog':dialog,
    'messages':reversed(messages),
    'dialog_with':dialog_with,
    'login_user':login_user,
    })