# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(unique=True, max_length=25)),
                ('email', models.EmailField(unique=True, max_length=50)),
                ('icon_URL', models.ImageField(upload_to=b'')),
                ('active', models.BooleanField(default=True)),
                ('member_since', models.DateTimeField(auto_now_add=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=127)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('album_id', models.ForeignKey(to='meows.Album')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purr_grr', models.CharField(blank=True, max_length=1, choices=[(b'p', b'purr'), (b'g', b'grr')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('from_user', models.ForeignKey(related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=254)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('hashtag_id', models.ForeignKey(to='meows.Hashtag')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creator', models.TextField(max_length=255)),
                ('contains_image', models.BooleanField(default=False)),
                ('image_URL', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('text_content', models.TextField(max_length=255)),
                ('score', models.IntegerField(default=0)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_edited', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('hashtags', models.ManyToManyField(to='meows.Hashtag')),
                ('purrs_grrs', models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='meows.Feedback')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='posts',
            name='post_id',
            field=models.ForeignKey(to='meows.User_Post'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='posts',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedback',
            name='post_id',
            field=models.ForeignKey(to='meows.User_Post'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedback',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(to='meows.User_Post'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='albums',
            name='post_id',
            field=models.ForeignKey(to='meows.User_Post'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='hashtags',
            field=models.ManyToManyField(to='meows.Hashtag', through='meows.Preference'),
            preserve_default=True,
        ),
    ]
