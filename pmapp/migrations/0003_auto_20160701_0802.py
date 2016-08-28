# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0002_auto_20160701_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workitem',
            name='itemid',
            field=models.IntegerField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True),
        ),
        migrations.AlterField(
            model_name='workitem',
            name='state',
            field=models.CharField(default=b'\xe8\xbf\x9b\xe8\xa1\x8c\xe4\xb8\xad', max_length=20, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'inprogress', b'\xe8\xbf\x9b\xe8\xa1\x8c\xe4\xb8\xad'), (b'done', b'\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90')]),
        ),
    ]
