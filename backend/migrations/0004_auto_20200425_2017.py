# Generated by Django 3.0.4 on 2020-04-26 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200424_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
