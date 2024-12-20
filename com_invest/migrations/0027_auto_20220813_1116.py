# Generated by Django 3.2.6 on 2022-08-13 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com_invest', '0026_investor_investmenthistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interesttypes',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='interesttypes',
            name='percentage',
        ),
        migrations.RemoveField(
            model_name='interesttypes',
            name='type',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='interestType',
        ),
        migrations.AddField(
            model_name='interesttypes',
            name='FixInterest',
            field=models.ManyToManyField(blank=True, related_name='fixList', to='com_invest.Investor'),
        ),
        migrations.AddField(
            model_name='interesttypes',
            name='GrowthInterest',
            field=models.ManyToManyField(blank=True, related_name='growthList', to='com_invest.Investor'),
        ),
        migrations.AddField(
            model_name='interesttypes',
            name='RatioInterest',
            field=models.ManyToManyField(blank=True, related_name='ratioList', to='com_invest.Investor'),
        ),
        migrations.AddField(
            model_name='interesttypes',
            name='Year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='investor',
            name='duration',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='investor',
            name='interest',
            field=models.FloatField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
