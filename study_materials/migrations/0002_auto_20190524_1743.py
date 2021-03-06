# Generated by Django 2.1.8 on 2019-05-24 11:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('study_materials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='free_materials',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='free_materials',
            name='belongs_to',
            field=models.CharField(choices=[('Science', 'SCINECE'), ('Commerce', 'COMMERCE'), ('Arts', 'ARTS'), ('All Subject', 'ALL SUBJECT')], default='Science', max_length=20),
        ),
    ]
