# Generated by Django 3.2.6 on 2021-09-12 18:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('com_sale', '0011_auto_20210912_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='i_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=64),
            preserve_default=False,
        ),
    ]
