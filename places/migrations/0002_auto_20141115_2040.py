# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='name',
            field=models.CharField(default=b'', max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='iwent',
            field=models.CharField(default=b'', max_length=120, blank=True),
            preserve_default=True,
        ),
    ]
