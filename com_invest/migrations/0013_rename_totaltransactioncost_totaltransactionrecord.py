# Generated by Django 3.2.6 on 2022-08-11 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('com_invest', '0012_totaltransactioncost_timestamp'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TotalTransactionCost',
            new_name='TotalTransactionRecord',
        ),
    ]
