# Generated by Django 3.2.7 on 2021-12-04 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0004_rename_user_car_userpk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='userPK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_car', to=settings.AUTH_USER_MODEL),
        ),
    ]
