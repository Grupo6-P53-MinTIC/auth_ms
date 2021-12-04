# Generated by Django 3.2.7 on 2021-12-04 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0005_alter_car_userpk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='userPK',
            new_name='userFK',
        ),
        migrations.RemoveField(
            model_name='car',
            name='id',
        ),
        migrations.AlterField(
            model_name='car',
            name='carRegistrationNumber',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
