# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20160517_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(max_length=1, choices=[(b'CEO', b'CEO'), (b'Manager', b'Manager'), (b'Project Lead', b'Project Lead'), (b'Software Developer', b'Software Developer'), (b'Junior Software Developer', b'Junior Software Developer'), (b'HR Manager', b'HR Manager'), (b'Quality Assurance Engineer', b'Quality Assurance Engineer')]),
            preserve_default=True,
        ),
    ]
