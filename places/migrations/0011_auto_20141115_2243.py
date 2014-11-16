# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_place_ref_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='place',
            unique_together=set([('ref_id', 'iwent', 'iam', 'igo')]),
        ),
    ]
