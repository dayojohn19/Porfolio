# Generated by Django 3.2.6 on 2021-09-12 16:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('com_sale', '0008_order_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='del_time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]