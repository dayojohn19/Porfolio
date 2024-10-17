# Generated by Django 3.2.6 on 2022-08-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com_invest', '0013_rename_totaltransactioncost_totaltransactionrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='SideComputations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MonthComputation', models.IntegerField(blank=True)),
                ('DateComputation', models.IntegerField(blank=True)),
                ('YearComputation', models.IntegerField(blank=True)),
                ('updatedTime', models.DateTimeField(blank=True)),
                ('startTime', models.DateTimeField(auto_now_add=True)),
                ('buy', models.ManyToManyField(blank=True, related_name='buying', to='com_invest.TotalTransactionRecord')),
                ('sell', models.ManyToManyField(blank=True, related_name='selling', to='com_invest.TotalTransactionRecord')),
            ],
        ),
    ]
