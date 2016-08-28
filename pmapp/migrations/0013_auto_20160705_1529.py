# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0012_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='content',
            field=models.TextField(max_length=50000, verbose_name=b'\xe7\xae\x80\xe6\x8a\xa5\xe5\x86\x85\xe5\xae\xb9'),
        ),
    ]
