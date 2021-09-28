# Generated by Django 3.2.6 on 2021-09-28 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g_pigeon_race', '0007_alter_record_clock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='clock',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='record',
            name='speed',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
