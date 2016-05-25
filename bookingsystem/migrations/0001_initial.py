# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_booked', models.IntegerField(choices=[(1, b'Conference Room number 1'), (2, b'Conference Room number 2'), (3, b'Conference Room number 3')])),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('booker_of_slot', models.ForeignKey(related_name='my_bookings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
