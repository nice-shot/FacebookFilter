# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed_filter', '0005_auto_20151002_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='name',
            field=models.CharField(help_text='Name to identify the filter by', max_length=200, default=0),
            preserve_default=False,
        ),
    ]
