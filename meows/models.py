from django.db import models
from django import forms
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


#class User(models.Model):
#    username = models.CharField(max_length = 25, unique= True)
#    owner_email = models.EmailField(max_length = 50, unique= True)
#    password = models.CharField(max_length = 50)
#    icon_URL = models.ImageField()
#    active = models.BooleanField(default = True)
#    member_since = models.DateTimeField(auto_now_add = True)
#    def __str__(self):
#        return self.username

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('User must have a valid email address')
        UN = self.normalize_email(email)
        if kwargs.get('username'):
            UN = kwargs.get('username')

        account = self.model(
            email = self.normalize_email(email), username=UN
        )

        account.set_password(password)
        account.save()
        
        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)
        account.is_admin = True
        account.save()

        return account

class User(AbstractBaseUser):
    email = models.EmailField(default="", unique=True)
    username = models.CharField(max_length=40, unique=True)

    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)

    is_admin = models.BooleanField(default=False)

    member_since = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQURIED_FIELDS = ['username']

    def _unicode_(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name


class User_Post(models.Model):
    contains_image = models.BooleanField(default = False)
    image_URL = models.ImageField(blank = True, null=True)
    text_content = models.TextField(max_length = 255)
    score = models.IntegerField(default = 0)
    time_created = models.DateTimeField(auto_now_add = True)
    time_edited = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)

    @staticmethod
    def create(text_cont):
        user_post = User_Post(text_content=text_cont)
        return user_post

class UserPostForm(forms.ModelForm):
    class Meta:
        model = User_Post

        fields = ["image_URL", "text_content"]

class Friends(models.Model):
    from_user = models.ForeignKey(User, related_name = 'from_user')
    to_user = models.ForeignKey(User, related_name = 'to_user')
    created = models.DateField(auto_now_add = True)

class Posts(models.Model):
    user_id = models.ForeignKey(User)
    post_id = models.ForeignKey(User_Post)

class Feedback(models.Model):
    FEEDBACK_OPTIONS = (
        ('l', 'like'),
        ('d', 'dislike'),
    )
    post_id = models.ForeignKey(User_Post)
    user_id = models.ForeignKey(User)
    like_dislike = models.CharField(max_length=1, choices=FEEDBACK_OPTIONS)

class Comment(models.Model):
    user_id = models.ForeignKey(User)
    post_id = models.ForeignKey(User_Post)
    content = models.TextField(max_length = 255)

class Album(models.Model):
    name = models.CharField(max_length = 127)

class Albums(models.Model):
    album_id = models.ForeignKey(Album)
    post_id = models.ForeignKey(User_Post)

