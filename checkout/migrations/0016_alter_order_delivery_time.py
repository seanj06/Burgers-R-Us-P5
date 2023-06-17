# Generated by Django 3.2.19 on 2023-06-16 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0015_auto_20230616_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.IntegerField(choices=[(datetime.time(15, 45), '15:45'), (datetime.time(16, 0), '16:00'), (datetime.time(16, 15), '16:15'), (datetime.time(16, 30), '16:30'), (datetime.time(16, 45), '16:45'), (datetime.time(17, 0), '17:00'), (datetime.time(17, 15), '17:15'), (datetime.time(17, 30), '17:30'), (datetime.time(17, 45), '17:45'), (datetime.time(18, 0), '18:00'), (datetime.time(18, 15), '18:15'), (datetime.time(18, 30), '18:30'), (datetime.time(18, 45), '18:45'), (datetime.time(19, 0), '19:00'), (datetime.time(19, 15), '19:15'), (datetime.time(19, 30), '19:30'), (datetime.time(19, 45), '19:45'), (datetime.time(20, 0), '20:00'), (datetime.time(20, 15), '20:15'), (datetime.time(20, 30), '20:30'), (datetime.time(20, 45), '20:45'), (datetime.time(21, 0), '21:00'), (datetime.time(21, 15), '21:15'), (datetime.time(21, 30), '21:30'), (datetime.time(21, 45), '21:45'), (datetime.time(22, 0), '22:00'), (datetime.time(22, 15), '22:15'), (datetime.time(22, 30), '22:30'), (datetime.time(22, 45), '22:45'), (datetime.time(23, 0), '23:00'), (datetime.time(23, 15), '23:15'), (datetime.time(23, 30), '23:30'), (datetime.time(23, 45), '23:45'), (datetime.time(0, 0), '00:00'), (datetime.time(0, 15), '00:15'), (datetime.time(0, 30), '00:30'), (datetime.time(0, 45), '00:45'), (datetime.time(1, 0), '01:00'), (datetime.time(1, 15), '01:15')], default=1),
        ),
    ]
