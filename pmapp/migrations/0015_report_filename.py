# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0014_auto_20160706_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='filename',
            field=models.CharField(max_length=500, null=True, verbose_name=b'\xe7\xae\x80\xe6\x8a\xa5\xe6\x96\x87\xe4\xbb\xb6\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
    ]
