# Generated by Django 3.2.6 on 2021-10-27 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('a_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_item',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
