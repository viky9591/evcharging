# Generated by Django 3.2 on 2021-06-20 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0004_stations_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='slots_table',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('station_id', models.IntegerField()),
            ],
        ),
    ]