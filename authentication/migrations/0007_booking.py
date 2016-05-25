# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20160516_0739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_booked', models.IntegerField(choices=[(1, b'Conference Room number 1'), (2, b'Conference Room number 2'), (3, b'Conference Room number 3')])),
                ('date_booked', models.DateField()),
                ('slot_booked', models.IntegerField(choices=[(9, b'9-10 am slot'), (10, b'10-11 am slot'), (11, b'11-12 am slot'), (12, b'12-1 pm slot'), (1, b'1-2 pm slot'), (2, b'2-3 pm slot'), (3, b'3-4 pm slot'), (4, b'4-5 pm slot'), (5, b'5-6 pm slot')])),
                ('booker_of_slot', models.ForeignKey(related_name='my_bookings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
