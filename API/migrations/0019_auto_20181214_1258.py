# Generated by Django 2.1.3 on 2018-12-14 11:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0018_auto_20181214_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Date',
            field=models.CharField(default=datetime.datetime(2018, 12, 14, 11, 58, 7, 325988, tzinfo=utc), max_length=250),
        ),
    ]