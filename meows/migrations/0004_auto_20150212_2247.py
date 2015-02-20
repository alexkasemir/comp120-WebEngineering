# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meows', '0003_auto_20150212_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_post',
            name='image_URL',
            field=models.ImageField(upload_to=b'/images'),
            preserve_default=True,
        ),
    ]
