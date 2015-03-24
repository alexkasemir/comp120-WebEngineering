# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meows', '0007_auto_20150305_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_post',
            name='image_URL',
            field=models.ImageField(null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
