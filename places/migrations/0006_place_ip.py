# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20141115_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='ip',
            field=models.CharField(default=b'ipX', max_length=40),
            preserve_default=True,
        ),
    ]
