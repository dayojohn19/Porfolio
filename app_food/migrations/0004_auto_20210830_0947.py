# Generated by Django 3.2.6 on 2021-08-30 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_food', '0003_auto_20210830_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tally',
            name='am',
            field=models.TextField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='tally',
            name='pm',
            field=models.TextField(blank=True, max_length=64, null=True),
        ),
    ]
