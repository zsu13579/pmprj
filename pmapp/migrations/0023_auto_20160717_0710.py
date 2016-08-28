# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0022_bossoverview_bossspec'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bossspec',
            options={'ordering': ['itemid'], 'verbose_name': '\u56fd\u6f2b\u4f18\u5316-\u9700\u6c42\u7f16\u5199', 'verbose_name_plural': '\u56fd\u6f2b\u4f18\u5316-\u9700\u6c42\u7f16\u5199'},
        ),
        migrations.AlterField(
            model_name='bossoverview',
            name='stage',
            field=models.IntegerField(default=1, verbose_name=b'\xe9\x98\xb6\xe6\xae\xb5', choices=[(1, b'\xe9\x9c\x80\xe6\xb1\x82\xe7\xbc\x96\xe5\x86\x99'), (2, b'\xe9\xaa\x8c\xe6\x94\xb6\xe6\xa1\x88\xe4\xbe\x8b\xe7\xbc\x96\xe5\x86\x99'), (3, b'\xe9\xaa\x8c\xe6\x94\xb6\xe4\xb8\x8a\xe7\xba\xbf'), (4, b'\xe8\xbf\x90\xe8\x90\xa5\xe6\xb5\x81\xe7\xa8\x8b\xe5\x88\xb6\xe5\xae\x9a')]),
        ),
    ]
