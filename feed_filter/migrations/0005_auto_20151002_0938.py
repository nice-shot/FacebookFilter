# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('feed_filter', '0004_auto_20151002_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookPage',
            fields=[
                ('id', models.CharField(serialize=False, primary_key=True, max_length=100, help_text="Page's facebook id")),
                ('name', models.CharField(help_text="Page or group's name", blank=True, max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='filter',
            name='filter_str',
            field=jsonfield.fields.JSONCharField(max_length=1000),
        ),
        migrations.AddField(
            model_name='filter',
            name='pages',
            field=models.ManyToManyField(to='feed_filter.FacebookPage', help_text='Pages to follow', related_name='+'),
        ),
        migrations.AddField(
            model_name='post',
            name='page',
            field=models.ForeignKey(to='feed_filter.FacebookPage', help_text='Page this post is from', default=0),
            preserve_default=False,
        ),
    ]
