# Generated by Django 3.2.6 on 2022-08-17 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com_invest', '0039_alter_sidecomputations_interestcomputation'),
    ]

    operations = [
        migrations.AddField(
            model_name='total_investment',
            name='portfolioValue',
            field=models.IntegerField(default=0),
        ),
    ]
