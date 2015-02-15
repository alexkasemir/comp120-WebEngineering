# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meows', '0002_auto_20150209_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon_URL',
            field=models.ImageField(upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_post',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
