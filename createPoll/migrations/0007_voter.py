# Generated by Django 3.0.7 on 2020-12-12 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('createPoll', '0006_delete_voter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votedBy', models.CharField(max_length=20)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='createPoll.Question')),
            ],
            options={
                'verbose_name_plural': 'Voter',
            },
        ),
    ]
