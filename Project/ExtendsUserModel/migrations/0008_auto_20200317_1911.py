# Generated by Django 3.0.3 on 2020-03-17 19:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExtendsUserModel', '0007_user_friend_requests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friend_requests',
        ),
        migrations.AddField(
            model_name='user',
            name='friend_requests_from',
            field=models.ManyToManyField(related_name='user_friend_requests_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='friend_requests_to',
            field=models.ManyToManyField(related_name='user_friend_requests_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
