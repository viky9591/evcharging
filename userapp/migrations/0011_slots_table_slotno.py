# Generated by Django 3.2 on 2021-06-26 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0010_alter_slots_table_station_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='slots_table',
            name='slotno',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
