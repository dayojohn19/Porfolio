# Generated by Django 3.2.6 on 2022-08-12 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com_invest', '0014_sidecomputations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sidecomputations',
            name='buy',
        ),
        migrations.RemoveField(
            model_name='sidecomputations',
            name='sell',
        ),
        migrations.AddField(
            model_name='sidecomputations',
            name='side',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sidecomputations',
            name='sideAmount',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sidecomputations',
            name='DateComputation',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='sidecomputations',
            name='MonthComputation',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='sidecomputations',
            name='updatedTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]