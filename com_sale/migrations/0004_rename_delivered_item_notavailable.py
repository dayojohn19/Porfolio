# Generated by Django 3.2.6 on 2021-09-11 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('com_sale', '0003_auto_20210911_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='delivered',
            new_name='notavailable',
        ),
    ]
