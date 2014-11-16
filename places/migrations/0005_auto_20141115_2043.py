# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20141115_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='name',
        ),
        migrations.AlterField(
            model_name='place',
            name='iam',
            field=models.CharField(default=b'Toulouse', max_length=120),
            preserve_default=True,
        ),
    ]
