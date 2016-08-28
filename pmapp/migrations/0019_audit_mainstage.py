# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0018_auto_20160708_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit',
            name='mainstage',
            field=models.IntegerField(default=1, verbose_name=b'\xe4\xb8\xbb\xe9\x98\xb6\xe6\xae\xb5', choices=[(1, b'\xe7\xac\xac\xe4\xb8\x80\xe9\x98\xb6\xe6\xae\xb5'), (2, b'\xe7\xac\xac\xe4\xba\x8c\xe9\x98\xb6\xe6\xae\xb5')]),
        ),
    ]
