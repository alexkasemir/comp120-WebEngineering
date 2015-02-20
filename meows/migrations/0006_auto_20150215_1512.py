# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meows', '0005_auto_20150213_1427'),
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
            name='image_URL',
            field=models.ImageField(upload_to=b''),
            preserve_default=True,
        ),
    ]
