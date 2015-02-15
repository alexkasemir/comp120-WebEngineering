# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
                ('created', models.DateField()),
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
                ('username', models.CharField(unique=True, max_length=25)),
                ('owner_email', models.EmailField(unique=True, max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('icon_URL', models.ImageField(height_field=50, width_field=50, upload_to=b'')),
                ('active', models.BooleanField()),
                ('member_since', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contains_image', models.BooleanField()),
                ('image_URL', models.ImageField(upload_to=b'')),
                ('text_content', models.TextField(max_length=255)),
                ('score', models.IntegerField()),
                ('time_created', models.DateField()),
                ('time_edited', models.DateField()),
                ('active', models.BooleanField()),
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
