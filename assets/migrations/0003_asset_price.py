# Generated by Django 3.1.4 on 2020-12-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20201212_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='current_price',
            field=models.FloatField(default=0),
        ),
    ]