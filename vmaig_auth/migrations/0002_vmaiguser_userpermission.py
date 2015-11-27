# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vmaig_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vmaiguser',
            name='userpermission',
            field=models.IntegerField(default=2, verbose_name=b'\xe4\xbc\x9a\xe5\x91\x98\xe6\x9d\x83\xe9\x99\x90', choices=[(0, '\u8d85\u7ea7VIP\u4f1a\u5458'), (1, 'VIP\u4f1a\u5458'), (2, '\u666e\u901a\u4f1a\u5458')]),
        ),
    ]
