# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meows', '0006_auto_20150215_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_post',
            name='image_URL',
            field=models.ImageField(null=True, upload_to=b'media'),
            preserve_default=True,
        ),
    ]
