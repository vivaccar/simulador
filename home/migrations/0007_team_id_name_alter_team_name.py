# Generated by Django 5.0.4 on 2024-05-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_game_round'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='id_name',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
