# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0017_auto_20160708_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audit',
            name='enddate',
            field=models.DateField(null=True, verbose_name=b'\xe5\xae\x9e\xe9\x99\x85\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xa5\xe6\x9c\x9f', blank=True),
        ),
    ]
