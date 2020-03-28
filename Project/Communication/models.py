from django.db import models
from ExtendsUserModel.models import User

class Message(models.Model):
    message_from = models.ForeignKey('ExtendsUserModel.User', on_delete=models.CASCADE, related_name='From', null=False)
    message_to = models.ForeignKey('ExtendsUserModel.User', on_delete=models.CASCADE, related_name='To', null=False)
    text = models.CharField(max_length=255, blank=False, null=False)
    is_read = models.BooleanField(default=False, null=False)
    time = models.DateTimeField(auto_now_add=True)

class Dialog(models.Model):
    connected_to = models.ForeignKey('ExtendsUserModel.User', on_delete=models.CASCADE, related_name="con_to", null=True)
    dialog_with = models.ForeignKey('ExtendsUserModel.User', on_delete=models.CASCADE, related_name="dial_with", null=True)
    messages = models.ManyToManyField('Communication.Message')