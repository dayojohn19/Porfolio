# Generated by Django 3.2.6 on 2022-08-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com_invest', '0020_total_investment_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='invested_percentage',
            field=models.IntegerField(default=0),
        ),
    ]
