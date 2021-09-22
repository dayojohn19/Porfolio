# Generated by Django 3.2.6 on 2021-09-21 08:29

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
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('clients', models.ManyToManyField(blank=True, default=None, related_name='bank_clients', to=settings.AUTH_USER_MODEL)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('manager', models.CharField(blank=True, max_length=63)),
                ('bank_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdraw_bank_id', to='com_bank.bank')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdraw_user', to='com_bank.bank')),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transaction_type', models.CharField(max_length=94)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('bank_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_bank_id', to='com_bank.bank')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_user', to='com_bank.bank')),
            ],
        ),
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('amount', models.IntegerField()),
                ('manager', models.CharField(max_length=94)),
                ('contact', models.CharField(max_length=94)),
                ('bank_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='com_bank.bank')),
                ('clients', models.ManyToManyField(blank=True, default=None, related_name='schedule_clients', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('bank_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_bank_id', to='com_bank.bank')),
            ],
        ),
    ]