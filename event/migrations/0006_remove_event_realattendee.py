# Generated by Django 5.0.2 on 2024-03-21 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_event_realattendee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='realAttendee',
        ),
    ]
