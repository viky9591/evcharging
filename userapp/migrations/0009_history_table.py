# Generated by Django 3.2 on 2021-06-26 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_alter_slots_table_chrging_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='history_table',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dateTime', models.DateTimeField()),
                ('username', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=15)),
                ('bookingNo', models.IntegerField()),
            ],
        ),
    ]
