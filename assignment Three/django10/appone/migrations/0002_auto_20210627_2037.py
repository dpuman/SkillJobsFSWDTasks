# Generated by Django 2.2.10 on 2021-06-27 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
