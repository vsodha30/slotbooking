# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20160513_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(max_length=1, choices=[(b'C', b'CEO'), (b'M', b'Manager'), (b'P', b'Project Lead'), (b'S', b'Software Developer'), (b'J', b'Junior Software Developer'), (b'H', b'HR Manager'), (b'Q', b'Quality Assurance Engineer')]),
            preserve_default=True,
        ),
    ]
