# Generated by Django 2.1.3 on 2018-11-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_order_whatever'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='whatever',
        ),
        migrations.AddField(
            model_name='order',
            name='OrderCreator',
            field=models.CharField(default='NOBODY', max_length=250),
        ),
    ]