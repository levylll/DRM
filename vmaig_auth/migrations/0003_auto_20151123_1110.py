# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vmaig_auth', '0002_vmaiguser_userpermission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vmaiguser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='vmaiguser',
            name='user_permissions',
        ),
    ]
