# Generated by Django 3.0.4 on 2020-04-29 05:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0016_event_interested'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='interested',
        ),
        migrations.AddField(
            model_name='event',
            name='interested',
            field=models.ManyToManyField(help_text='who is interested', related_name='interested', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ManyToManyField(help_text='add organizer', related_name='organizer', to=settings.AUTH_USER_MODEL),
        ),
    ]
