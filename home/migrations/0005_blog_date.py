# Generated by Django 2.1.8 on 2019-05-22 22:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]