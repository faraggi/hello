# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_place_ip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='ip',
            new_name='ip_address',
        ),
    ]
