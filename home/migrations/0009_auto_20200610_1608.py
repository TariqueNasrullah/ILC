# Generated by Django 2.1.8 on 2020-06-10 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200610_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_information',
            name='message',
            field=models.TextField(default='', max_length=1200),
        ),
    ]
