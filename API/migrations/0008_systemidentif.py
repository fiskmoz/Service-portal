# Generated by Django 2.1.3 on 2018-12-12 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_resources'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemIdentif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SystemID', models.CharField(default=None, max_length=50)),
                ('Owner', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
