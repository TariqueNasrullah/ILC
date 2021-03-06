# Generated by Django 2.1.8 on 2020-09-08 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('subject', models.CharField(max_length=256)),
                ('university', models.CharField(max_length=256)),
                ('batch', models.IntegerField()),
                ('student_photo', models.ImageField(blank=True, upload_to='imageFiles')),
            ],
        ),
    ]
