# Generated by Django 3.0.7 on 2020-12-12 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createPoll', '0002_auto_20201212_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pollBy',
            field=models.CharField(default='anonymous', max_length=20),
        ),
    ]
