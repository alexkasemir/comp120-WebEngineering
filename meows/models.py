from django.db import models
#from django import forms
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import UserManager


class Hashtag(models.Model):
    content = models.CharField(max_length=254)
    count = models.IntegerField(default=0)





class User(AbstractBaseUser):
    #user = models.OneToOneField(User)
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    #password = models.CharField(max_length = 50)
    icon_URL = models.ImageField()
    active = models.BooleanField(default=True)
    member_since = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    objects = UserManager()
    hashtags = models.ManyToManyField(Hashtag, through='Preference')

    def __str__(self):
        return self.username

    def _unicode_(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name


class Preference(models.Model):
    user_id = models.ForeignKey(User)
    hashtag_id = models.ForeignKey(Hashtag)
    score = models.IntegerField(default=0)


class User_Post(models.Model):
    creator = models.TextField(max_length=255)
    contains_image = models.BooleanField(default=False)
    image_URL = models.ImageField(blank=True, null=True)
    text_content = models.TextField(max_length=255)
    score = models.IntegerField(default=0)
    time_created = models.DateTimeField(auto_now_add=True)
    time_edited = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    purrs_grrs = models.ManyToManyField(User, through='Feedback')
    hashtags = models.ManyToManyField(Hashtag)
    # grrs = models.ManyToManyField(User, related_name='grrs', through='Dislike')

    @staticmethod
    def create(text_cont):
        user_post = User_Post(text_content=text_cont)
        return user_post


class Feedback(models.Model):
    FEEDBACK_OPTIONS = (
        ('p', 'purr'),
        ('g', 'grr'),
    )
    post_id = models.ForeignKey(User_Post)
    user_id = models.ForeignKey(User)
    purr_grr = models.CharField(max_length=1, choices=FEEDBACK_OPTIONS, blank=True)


class Friends(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user')
    to_user = models.ForeignKey(User, related_name='to_user')
    created = models.DateField(auto_now_add=True)


class Posts(models.Model):
    user_id = models.ForeignKey(User)
    post_id = models.ForeignKey(User_Post)


class Comment(models.Model):
    user_id = models.ForeignKey(User)
    post_id = models.ForeignKey(User_Post)
    content = models.TextField(max_length=255)

class Album(models.Model):
    name = models.CharField(max_length=127)

class Albums(models.Model):
    album_id = models.ForeignKey(Album)
    post_id = models.ForeignKey(User_Post)

