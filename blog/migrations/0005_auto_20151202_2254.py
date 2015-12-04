# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='file',
            field=models.FileField(null=True, upload_to=b'./static/upload/', blank=True),
        ),
    ]
