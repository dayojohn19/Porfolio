# Generated by Django 3.2.6 on 2021-12-16 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_freedive', '0004_events_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Event_Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('room_name', models.CharField(max_length=64)),
                ('room_participants', models.ManyToManyField(blank=True, default=None, related_name='participants', to='app_freedive.Participants')),
            ],
        ),
        migrations.CreateModel(
            name='Event_Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('sender', models.CharField(max_length=64)),
                ('sender_image', models.URLField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('chat_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_freedive.events')),
            ],
        ),
    ]
