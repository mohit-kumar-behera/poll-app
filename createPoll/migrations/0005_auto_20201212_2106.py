# Generated by Django 3.0.7 on 2020-12-12 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('createPoll', '0004_voter_selectedchoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='selectedChoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createPoll.Choices'),
        ),
    ]