# Generated by Django 3.2.6 on 2022-05-15 02:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_Car', '0008_auto_20220514_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeschedule',
            name='monthNN',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]