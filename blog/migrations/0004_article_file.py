# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151129_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='file',
            field=models.FileField(null=True, upload_to=b'./upload/', blank=True),
        ),
    ]
