# Generated by Django 3.2.6 on 2022-08-14 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('com_invest', '0033_auto_20220814_0226'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GiveDividends',
            new_name='DividendRecord',
        ),
    ]