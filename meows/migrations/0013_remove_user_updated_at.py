# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meows', '0012_auto_20150401_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
    ]
