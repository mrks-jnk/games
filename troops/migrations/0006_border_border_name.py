# Generated by Django 3.0.8 on 2020-07-07 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('troops', '0005_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='border',
            name='border_name',
            field=models.CharField(default='border', max_length=20),
        ),
    ]
