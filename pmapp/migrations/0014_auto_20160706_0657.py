# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0013_auto_20160705_1529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['-reportid'], 'verbose_name': '\u5de5\u4f5c\u7b80\u62a5', 'verbose_name_plural': '\u5de5\u4f5c\u7b80\u62a5'},
        ),
        migrations.AddField(
            model_name='report',
            name='file',
            field=models.FileField(upload_to=b'report/', null=True, verbose_name=b'\xe7\xae\x80\xe6\x8a\xa5\xe6\x96\x87\xe4\xbb\xb6', blank=True),
        ),
    ]
