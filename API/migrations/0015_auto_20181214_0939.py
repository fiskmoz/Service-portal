# Generated by Django 2.1.3 on 2018-12-14 08:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0014_auto_20181214_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Date',
            field=models.CharField(default=datetime.datetime(2018, 12, 14, 8, 39, 46, 810711, tzinfo=utc), max_length=250),
        ),
    ]
