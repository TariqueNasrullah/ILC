# Generated by Django 2.1.8 on 2020-09-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200610_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_photo',
            field=models.ImageField(blank=True, upload_to='imageFiles'),
        ),
        migrations.AddField(
            model_name='blog',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='university',
            field=models.CharField(default='', max_length=100),
        ),
    ]
