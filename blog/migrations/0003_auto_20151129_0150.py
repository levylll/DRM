# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150514_2229'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['rank', '-is_top', '-pub_time', '-create_time'], 'verbose_name': '\u5185\u5bb9', 'verbose_name_plural': '\u5185\u5bb9'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['rank', '-create_time'], 'verbose_name': '\u7c7b\u522b', 'verbose_name_plural': '\u7c7b\u522b'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='img',
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='\u7c7b\u522b', to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(null=True, verbose_name='\u5185\u5bb9', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='en_title',
            field=models.CharField(help_text='\u7cfb\u7edf\u5185\u90e8\u7684\u552f\u4e00\u6807\u793a,\u975e\u5e38\u91cd\u8981,\u4f7f\u7528\u82f1\u6587\u6216\u8005\u6570\u5b57', max_length=100, verbose_name='\u82f1\u6587\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(null=True, verbose_name='\u6458\u8981', blank=True),
        ),
    ]
