# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed_filter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='relative_id',
            field=models.PositiveIntegerField(help_text='ID is unique per user'),
        ),
    ]
