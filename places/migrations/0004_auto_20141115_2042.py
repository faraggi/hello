# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20141115_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='iam',
            field=models.CharField(default=b'', max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='igo',
            field=models.CharField(default=b'', max_length=120, blank=True),
            preserve_default=True,
        ),
    ]
