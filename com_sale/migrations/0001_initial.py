# Generated by Django 3.2.6 on 2021-10-14 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='fancier')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notavailable', models.BooleanField(default=False)),
                ('listing_date', models.DateTimeField()),
                ('paid_date', models.IntegerField()),
                ('expiration_date', models.DateTimeField()),
                ('title', models.CharField(max_length=64)),
                ('owner', models.CharField(max_length=64)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('link', models.URLField()),
                ('link2', models.URLField(blank=True)),
                ('link3', models.URLField(blank=True)),
                ('link4', models.URLField(blank=True)),
                ('link5', models.URLField(blank=True)),
                ('link6', models.URLField(blank=True)),
                ('link7', models.URLField(blank=True)),
                ('link8', models.URLField(blank=True)),
                ('link9', models.URLField(blank=True)),
                ('link10', models.URLField(blank=True)),
                ('description', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=64)),
                ('bought', models.IntegerField(default=0)),
                ('orders', models.ManyToManyField(blank=True, default=None, related_name='item_order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Userimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='fancier_profiles')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='com_sale.item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_id', models.CharField(max_length=64)),
                ('i_price', models.IntegerField(default=1)),
                ('i_total_price', models.IntegerField(default=2)),
                ('owner', models.CharField(max_length=64)),
                ('select', models.URLField(blank=True)),
                ('delivered', models.BooleanField(default=False)),
                ('del_time', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField()),
                ('qty', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='com_sale.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
