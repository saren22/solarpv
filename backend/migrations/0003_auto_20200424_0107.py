# Generated by Django 3.0.4 on 2020-04-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200405_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cell_phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='job_title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='office_phone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
