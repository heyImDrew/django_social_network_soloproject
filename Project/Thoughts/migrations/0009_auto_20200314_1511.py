# Generated by Django 3.0.3 on 2020-03-14 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Thoughts', '0008_comment_connected_person_to_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='connected_person_to_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserToPost', to=settings.AUTH_USER_MODEL),
        ),
    ]
