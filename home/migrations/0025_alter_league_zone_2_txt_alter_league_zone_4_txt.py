# Generated by Django 5.0.4 on 2024-05-30 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_league_zone_3_txt_alter_league_zone_5_txt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='zone_2_txt',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='league',
            name='zone_4_txt',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
    ]
