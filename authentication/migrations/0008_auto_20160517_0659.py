# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booker_of_slot',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
