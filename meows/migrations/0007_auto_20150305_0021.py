# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meows', '0006_auto_20150215_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='member_since',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_post',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_post',
            name='time_edited',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
