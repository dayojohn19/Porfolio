# Generated by Django 3.2.6 on 2021-12-15 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=64)),
                ('end_time', models.CharField(max_length=64)),
                ('organizer', models.CharField(max_length=64)),
                ('event_type', models.CharField(max_length=64)),
                ('event_name', models.CharField(max_length=64)),
                ('event_description', models.CharField(max_length=500)),
            ],
        ),
    ]