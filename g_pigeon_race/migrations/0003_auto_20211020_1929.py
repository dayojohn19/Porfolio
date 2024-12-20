# Generated by Django 3.2.6 on 2021-10-20 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('g_pigeon_race', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='clock',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='record',
            name='distance',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='record',
            name='lap_id',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='lap_name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='record',
            name='pigeon_id',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='record',
            name='pigeon_name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='record',
            name='race',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='record',
            name='race_name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='record',
            name='release',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='record',
            name='ring',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
