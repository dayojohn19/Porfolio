# Generated by Django 3.2.6 on 2022-05-15 02:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ship_san_diego', '0014_alter_mysandiegodays_datenow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysandiegodays',
            name='dateNow',
            field=models.DateField(default=datetime.datetime(2022, 5, 15, 2, 34, 56, 5810)),
        ),
    ]