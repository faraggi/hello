# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_auto_20141115_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='ref_id',
            field=models.CharField(default=b'XXX', unique=True, max_length=40),
            preserve_default=True,
        ),
    ]
