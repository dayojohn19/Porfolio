# Generated by Django 3.2.6 on 2022-05-15 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_Car', '0009_placeschedule_monthnn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placeschedule',
            name='monthNN',
        ),
    ]
