# Generated by Django 4.0.3 on 2022-05-07 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0002_profile_email_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]