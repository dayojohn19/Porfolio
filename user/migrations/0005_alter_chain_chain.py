# Generated by Django 3.2.6 on 2021-09-24 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_chain_chain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chain',
            name='chain',
            field=models.CharField(default=1231, max_length=64),
        ),
    ]