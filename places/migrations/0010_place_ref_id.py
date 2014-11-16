# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_place_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='ref_id',
            field=models.CharField(default=b'XXX', max_length=40),
            preserve_default=True,
        ),
    ]
