# Generated by Django 3.2.6 on 2021-08-25 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64)),
                ('hcode', models.CharField(max_length=64)),
                ('ring_code', models.CharField(blank=True, max_length=64)),
                ('pigeon_id', models.CharField(blank=True, max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('ring', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=100)),
                ('linkimage', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_lat', models.CharField(max_length=64)),
                ('release_long', models.CharField(max_length=64)),
                ('released', models.BooleanField(default=False)),
                ('release_time', models.CharField(blank=True, max_length=64)),
                ('loading_cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Loaded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_id', models.CharField(max_length=64)),
                ('race_name', models.CharField(max_length=64)),
                ('lap', models.CharField(max_length=64)),
                ('lap_name', models.CharField(max_length=64)),
                ('pigeon_id', models.CharField(max_length=65)),
                ('pigeon_name', models.CharField(max_length=64)),
                ('pigeon_ring', models.CharField(blank=True, max_length=64)),
                ('pigeon_hcode', models.CharField(blank=True, max_length=64)),
                ('pigeon_lat', models.CharField(max_length=64)),
                ('pigeon_long', models.CharField(max_length=64)),
                ('pigeon_loader', models.CharField(max_length=64)),
                ('release_lat', models.CharField(max_length=64)),
                ('release_long', models.CharField(max_length=64)),
                ('release_time', models.CharField(blank=True, max_length=64)),
                ('clock_time', models.CharField(blank=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('latitude', models.CharField(max_length=64)),
                ('longitude', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=64)),
                ('place_lat', models.CharField(max_length=64)),
                ('place_long', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('racename', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ring', models.CharField(max_length=50)),
                ('pigeon_name', models.CharField(max_length=64)),
                ('lap_id', models.CharField(max_length=50)),
                ('lap_name', models.CharField(max_length=64)),
                ('race', models.CharField(max_length=64)),
                ('race_name', models.CharField(max_length=64)),
                ('release', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=64)),
                ('clock', models.CharField(max_length=50)),
                ('speed', models.CharField(max_length=50)),
                ('distance', models.CharField(max_length=64)),
            ],
        ),
    ]