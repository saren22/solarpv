# Generated by Django 3.0.4 on 2020-04-27 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20200425_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='certificate_number',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='client_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='location_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='model_number',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='test_standard',
            name='standard_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
