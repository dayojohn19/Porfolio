# Generated by Django 3.2.6 on 2022-01-03 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20211204_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=64)),
                ('contact', models.CharField(blank=True, max_length=64)),
                ('visit_count', models.IntegerField(default=1)),
            ],
        ),
    ]
