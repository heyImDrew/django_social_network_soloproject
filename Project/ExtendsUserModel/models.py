from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True, width_field=325, height_field=325)
    friend_requests_from = models.ManyToManyField('User', related_name='user_friend_requests_from', blank=True)
    friend_requests_to = models.ManyToManyField('User', related_name='user_friend_requests_to', blank=True)
    friends = models.ManyToManyField('User', related_name='user_friends', blank=True)