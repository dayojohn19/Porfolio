# Generated by Django 3.2.6 on 2022-08-06 07:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ship_san_diego', '0019_alter_mysandiegodays_datenow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysandiegodays',
            name='dateNow',
            field=models.DateField(default=datetime.datetime(2022, 8, 6, 7, 25, 54, 506780)),
        ),
    ]
