# Generated by Django 3.2.6 on 2021-08-30 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_food', '0006_auto_20210830_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(max_length=64)),
                ('umaga', models.TextField(max_length=64)),
                ('tanghali', models.TextField(max_length=64)),
                ('gabi', models.TextField(max_length=64)),
            ],
        ),
    ]
