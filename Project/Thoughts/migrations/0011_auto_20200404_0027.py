# Generated by Django 3.0.3 on 2020-04-04 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Thoughts', '0010_post_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(to='Thoughts.Comment'),
        ),
    ]
