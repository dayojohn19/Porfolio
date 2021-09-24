# Generated by Django 3.2.6 on 2021-09-24 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com_sale', '0016_order_i_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='duration',
            field=models.DurationField(default=3, verbose_name=datetime.timedelta(days=20, seconds=36000)),
        ),
    ]
