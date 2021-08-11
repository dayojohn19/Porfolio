# Generated by Django 3.2.2 on 2021-08-09 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_street_race', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_id',
            new_name='room_code',
        ),
        migrations.AlterField(
            model_name='room',
            name='player1',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='room',
            name='player2',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
