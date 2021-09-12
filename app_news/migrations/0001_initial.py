# Generated by Django 3.2.6 on 2021-09-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=64)),
                ('link', models.CharField(max_length=6464)),
                ('content', models.TextField()),
            ],
        ),
    ]