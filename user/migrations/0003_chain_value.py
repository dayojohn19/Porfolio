# Generated by Django 3.2.6 on 2021-09-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_chain'),
    ]

    operations = [
        migrations.AddField(
            model_name='chain',
            name='value',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
