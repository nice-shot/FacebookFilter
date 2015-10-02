# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed_filter', '0002_auto_20150930_0944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filteredpost',
            old_name='interesting',
            new_name='keep',
        ),
        migrations.AlterUniqueTogether(
            name='filter',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='filter',
            name='relative_id',
        ),
    ]
