# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmapp', '0010_auto_20160701_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('meetingid', models.IntegerField(serialize=False, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7', primary_key=True)),
                ('date', models.DateField(verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('memo', models.TextField(max_length=5000, verbose_name=b'\xe4\xbc\x9a\xe8\xae\xae\xe7\xba\xaa\xe8\xa6\x81')),
                ('attender', models.TextField(max_length=1000, verbose_name=b'\xe5\x8f\x82\xe4\xbc\x9a\xe4\xba\xba\xe5\x91\x98')),
                ('type', models.IntegerField(choices=[(1, b'\xe6\x97\xa5\xe5\xb8\xb8\xe4\xba\xa4\xe6\xb5\x81'), (2, b'\xe9\x9b\x86\xe5\x9b\xa2\xe4\xbc\x9a\xe8\xae\xae'), (3, b'\xe9\xab\x98\xe5\xb1\x82\xe4\xbc\x9a\xe8\xae\xae')])),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': '\u4f1a\u8bae\u60c5\u51b5',
                'verbose_name_plural': '\u4f1a\u8bae\u60c5\u51b5',
            },
        ),
    ]
