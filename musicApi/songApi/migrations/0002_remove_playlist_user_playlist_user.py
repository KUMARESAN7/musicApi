# Generated by Django 4.2.3 on 2023-07-09 12:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='user',
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ManyToManyField(related_name='playlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
