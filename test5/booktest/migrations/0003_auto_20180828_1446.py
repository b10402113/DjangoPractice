# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_areainfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areainfo',
            name='aPArea',
            field=models.ForeignKey(blank=True, null=True, to='booktest.AreaInfo'),
        ),
    ]
