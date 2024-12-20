# Generated by Django 3.2.6 on 2022-08-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com_invest', '0006_stockshand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockshand',
            name='stockBuyPrice',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='total_investment',
            name='average',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
