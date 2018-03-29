# Generated by Django 2.0.3 on 2018-03-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0005_auto_20180328_0601'),
    ]

    operations = [
        migrations.CreateModel(
            name='elec_emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='abc', max_length=25)),
                ('free', models.CharField(default='0000-00-00-00', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='furni_emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='abc', max_length=25)),
                ('free', models.CharField(default='0000-00-00-00', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='water_emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='abc', max_length=25)),
                ('free', models.CharField(default='0000-00-00-00', max_length=50)),
            ],
        ),
    ]