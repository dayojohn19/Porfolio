# Generated by Django 3.2.6 on 2022-08-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com_invest', '0008_auto_20220810_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='investmentrecord',
            name='invest_valueBefore',
            field=models.IntegerField(default=0),
        ),
    ]