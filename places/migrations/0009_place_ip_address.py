# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_remove_place_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='ip_address',
            field=models.CharField(default=b'ipX', max_length=40),
            preserve_default=True,
        ),
    ]
