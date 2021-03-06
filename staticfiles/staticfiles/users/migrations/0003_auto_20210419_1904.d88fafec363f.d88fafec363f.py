# Generated by Django 3.1.7 on 2021-04-20 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_app_imageapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='imageApp',
            field=models.ImageField(blank=True, default='', null=True, upload_to='static/img/bd/app'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, default='', null=True, upload_to='static/img/bd/user'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(default='default', max_length=255),
        ),
    ]
