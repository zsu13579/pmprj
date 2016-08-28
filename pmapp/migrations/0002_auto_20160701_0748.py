# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workitem',
            options={'ordering': ['itemid'], 'verbose_name': '\u91cd\u70b9\u5de5\u4f5c\u8fdb\u5c55\u60c5\u51b5', 'verbose_name_plural': '\u91cd\u70b9\u5de5\u4f5c\u8fdb\u5c55\u60c5\u51b5'},
        ),
        migrations.AddField(
            model_name='workitem',
            name='name',
            field=models.CharField(default='test', max_length=500, verbose_name=b'\xe4\xba\x8b\xe5\xae\x9c'),
            preserve_default=False,
        ),
    ]
