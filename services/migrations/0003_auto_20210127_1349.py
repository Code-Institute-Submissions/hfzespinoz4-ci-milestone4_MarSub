# Generated by Django 3.1.5 on 2021-01-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20210127_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='image',
        ),
        migrations.AlterField(
            model_name='services',
            name='image_url',
            field=models.CharField(max_length=1024),
        ),
    ]