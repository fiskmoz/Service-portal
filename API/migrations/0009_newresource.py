# Generated by Django 2.1.3 on 2018-12-12 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_systemidentif'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Object', models.CharField(max_length=50)),
                ('OS', models.CharField(max_length=50)),
                ('Packet', models.CharField(max_length=50)),
                ('system', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='API.SystemIdentif')),
            ],
        ),
    ]
