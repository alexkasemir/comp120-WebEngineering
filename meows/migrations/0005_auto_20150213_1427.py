# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meows', '0004_auto_20150212_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon_URL',
            field=models.ImageField(upload_to=b'/images'),
            preserve_default=True,
        ),
    ]
