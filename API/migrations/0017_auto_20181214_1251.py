# Generated by Django 2.1.3 on 2018-12-14 11:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0016_auto_20181214_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreements',
            name='OrderName',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='API.Order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='Date',
            field=models.CharField(default=datetime.datetime(2018, 12, 14, 11, 51, 37, 582771, tzinfo=utc), max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='OrderName',
            field=models.CharField(default='defaultordername', max_length=250),
        ),
    ]
