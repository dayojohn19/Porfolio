# Generated by Django 3.2.6 on 2022-08-12 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com_invest', '0019_auto_20220812_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='total_investment',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]