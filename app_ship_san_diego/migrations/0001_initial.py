# Generated by Django 3.2.6 on 2022-03-17 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('user_picture', models.URLField(blank=True)),
                ('contact', models.CharField(max_length=64)),
                ('say', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MySandiegoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_id', models.IntegerField(default=0)),
                ('poster_name', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('value', models.IntegerField()),
                ('location', models.CharField(max_length=64)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MySanDiegoDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_id', models.IntegerField(default=1)),
                ('poster', models.CharField(blank=True, max_length=64)),
                ('title', models.CharField(blank=True, max_length=24)),
                ('feeling', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('dateUpdated', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(blank=True, max_length=64)),
                ('vicinity', models.CharField(blank=True, max_length=64)),
                ('courseTrue', models.IntegerField(blank=True, null=True)),
                ('speed', models.IntegerField(blank=True, null=True)),
                ('DutiesAndEvents', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='san_diego')),
                ('activity', models.TextField(blank=True, null=True)),
                ('latitude', models.CharField(blank=True, max_length=64)),
                ('longitude', models.CharField(blank=True, max_length=64)),
                ('comments', models.ManyToManyField(blank=True, related_name='comments', to='app_ship_san_diego.Comment')),
            ],
        ),
    ]
