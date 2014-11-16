# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20141115_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='ip_address',
        ),
    ]
