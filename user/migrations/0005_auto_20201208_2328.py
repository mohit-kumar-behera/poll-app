# Generated by Django 3.0.7 on 2020-12-08 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201208_2137'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='quickPollUser',
        ),
    ]
