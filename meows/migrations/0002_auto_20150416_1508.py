# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('meows', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='like_dislike',
        ),
        migrations.AddField(
            model_name='feedback',
            name='purr_grr',
            field=models.CharField(blank=True, max_length=1, choices=[(b'p', b'purr'), (b'g', b'grr')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_post',
            name='purrs_grrs',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='meows.Feedback'),
            preserve_default=True,
        ),
    ]
