# Generated by Django 3.2.7 on 2021-12-04 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='user',
            new_name='userPK',
        ),
    ]
