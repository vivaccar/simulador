# Generated by Django 5.0.4 on 2024-05-13 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_game_away_logo_game_home_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='timestamp',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]