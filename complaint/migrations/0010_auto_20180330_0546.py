# Generated by Django 2.0 on 2018-03-30 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0009_auto_20180330_0542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otp',
            old_name='otp',
            new_name='otp_number',
        ),
    ]
