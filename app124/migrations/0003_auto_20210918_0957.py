# Generated by Django 3.0.1 on 2021-09-18 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app124', '0002_auto_20210918_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='profile_image',
            field=models.ImageField(upload_to='my_image/'),
        ),
    ]
