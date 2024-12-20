# Generated by Django 3.2.6 on 2021-12-26 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investor_name', models.CharField(max_length=64)),
                ('investor_contact', models.CharField(max_length=64)),
                ('invested_percentage', models.IntegerField()),
                ('invested_amount', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Total_Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('average', models.IntegerField(blank=True)),
                ('quantity', models.IntegerField(blank=True)),
                ('stock', models.CharField(max_length=64)),
            ],
        ),
    ]
