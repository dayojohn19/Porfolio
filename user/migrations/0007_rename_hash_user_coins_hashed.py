# Generated by Django 3.2.6 on 2021-12-04 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_coins'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_coins',
            old_name='hash',
            new_name='hashed',
        ),
    ]
