# Generated by Django 3.0.8 on 2020-07-19 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_api', '0003_auto_20200719_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birthdate',
        ),
    ]
