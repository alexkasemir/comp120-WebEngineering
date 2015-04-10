# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
                ('like_dislike', models.CharField(max_length=1, choices=[(b'l', b'like'), (b'd', b'dislike')])),
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
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(unique=True, max_length=25)),
                ('owner_email', models.EmailField(unique=True, max_length=50)),
                ('icon_URL', models.ImageField(upload_to=b'')),
                ('active', models.BooleanField(default=True)),
                ('member_since', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contains_image', models.BooleanField(default=False)),
                ('image_URL', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('text_content', models.TextField(max_length=255)),
                ('score', models.IntegerField(default=0)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('time_edited', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
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
            field=models.ForeignKey(to='meows.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friends',
            name='from_user',
            field=models.ForeignKey(related_name='from_user', to='meows.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='friends',
            name='to_user',
            field=models.ForeignKey(related_name='to_user', to='meows.User'),
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
            field=models.ForeignKey(to='meows.User'),
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
            field=models.ForeignKey(to='meows.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='albums',
            name='post_id',
            field=models.ForeignKey(to='meows.User_Post'),
            preserve_default=True,
        ),
    ]
