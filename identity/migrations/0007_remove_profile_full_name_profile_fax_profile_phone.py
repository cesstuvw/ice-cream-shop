# Generated by Django 4.0.3 on 2022-05-07 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0006_remove_profile_email_remove_profile_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='full_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='fax',
            field=models.CharField(max_length=40, null=True, verbose_name='Fax'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=40, null=True, verbose_name='Phone'),
        ),
    ]
