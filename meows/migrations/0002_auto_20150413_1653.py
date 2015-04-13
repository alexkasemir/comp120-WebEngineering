# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meows', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='owner_email',
            new_name='email',
        ),
    ]
