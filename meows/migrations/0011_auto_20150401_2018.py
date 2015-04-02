# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meows', '0010_auto_20150331_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='icon_URL',
        ),
        migrations.RemoveField(
            model_name='user',
            name='owner_email',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=b'', unique=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=40, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(unique=True, max_length=40),
            preserve_default=True,
        ),
    ]
