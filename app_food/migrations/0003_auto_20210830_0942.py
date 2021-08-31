# Generated by Django 3.2.6 on 2021-08-30 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_food', '0002_auto_20210830_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tally',
            name='date',
        ),
        migrations.RemoveField(
            model_name='tally',
            name='day',
        ),
        migrations.RemoveField(
            model_name='tally',
            name='food',
        ),
        migrations.RemoveField(
            model_name='tally',
            name='noon',
        ),
        migrations.AddField(
            model_name='tally',
            name='am',
            field=models.TextField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='tally',
            name='pm',
            field=models.TextField(blank=True, max_length=64),
        ),
    ]