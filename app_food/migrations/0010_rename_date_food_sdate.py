# Generated by Django 3.2.6 on 2021-08-30 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_food', '0009_auto_20210830_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='date',
            new_name='sdate',
        ),
    ]
