# Generated by Django 3.0.3 on 2020-04-04 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Thoughts', '0014_auto_20200404_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='connected_person_to_post',
        ),
    ]
