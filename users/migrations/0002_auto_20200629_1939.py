# Generated by Django 3.0.6 on 2020-06-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(default="Hey there! I'm on django blog", max_length=300),
        ),
    ]
