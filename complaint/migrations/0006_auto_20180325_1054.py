# Generated by Django 2.0 on 2018-03-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0005_auto_20180325_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='st_16ca6001',
            name='status',
            field=models.CharField(default='Registered', max_length=10),
        ),
    ]