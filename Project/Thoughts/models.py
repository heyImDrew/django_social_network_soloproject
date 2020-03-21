from django.db import models
from ExtendsUserModel.models import User
 
class Post(models.Model):
    connected_to = models.ForeignKey('ExtendsUserModel.User', on_delete=models.CASCADE, related_name='User')
    text = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    connected_to_post = models.ForeignKey('Thoughts.Post', on_delete=models.CASCADE, related_name='CommentPost')
    connected_person_to_post = models.ForeignKey('ExtendsUserModel.User', on_delete=models.CASCADE, related_name='UserToPost')
    connected_to = models.ForeignKey('ExtendsUserModel.User', on_delete=models.CASCADE, related_name='CommentUser')
    text = models.CharField(max_length=255)