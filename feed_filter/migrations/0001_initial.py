# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('relative_id', models.PositiveIntegerField(help_text='Unique filter ID per user')),
                ('filter_str', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='filters')),
            ],
        ),
        migrations.CreateModel(
            name='FilteredPost',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('found_time', models.DateTimeField(auto_now_add=True)),
                ('interesting', models.NullBooleanField()),
                ('comment', models.TextField(blank=True)),
                ('filter', models.ForeignKey(to='feed_filter.Filter')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=100, help_text='Facebook post id', serialize=False)),
                ('message', models.TextField()),
                ('user', models.CharField(help_text='Facebook user name', max_length=300)),
                ('created_time', models.DateTimeField()),
                ('updated_time', models.DateTimeField()),
                ('filters', models.ManyToManyField(to='feed_filter.Filter', related_name='posts', through='feed_filter.FilteredPost')),
            ],
        ),
        migrations.AddField(
            model_name='filteredpost',
            name='post',
            field=models.ForeignKey(to='feed_filter.Post'),
        ),
        migrations.AlterUniqueTogether(
            name='filter',
            unique_together=set([('user', 'relative_id')]),
        ),
    ]
