# Generated by Django 2.0 on 2018-03-30 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0008_auto_20180330_0514'),
    ]

    operations = [
        migrations.CreateModel(
            name='otp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField()),
                ('user_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='elec_emp',
        ),
        migrations.DeleteModel(
            name='furni_emp',
        ),
        migrations.DeleteModel(
            name='water_emp',
        ),
    ]