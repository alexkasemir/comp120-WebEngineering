from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 25, unique= true)
    owner_email = models.EmailField(max_length = 50, unique= true)
    password = models.CharField(max_length = 50)
    icon_URL = models.ImageField(upload_to = "", height_field = 50px, width_field = 50px)
    active = models.BooleanField()
    member_since = models.DateField()
    def __str__(self):
        return self.username

class User_Post(models.Model):
    contains_image = models.BooleanField()
    image_URL = models.ImageField(upload_to = "")
    text_content = models.TextField(max_length = 255)
    score = models.IntegerField()
    time_created = models.DateField()
    time_edited = models.DateField()
    active = models.BooleanField()

class Friends(models.Model):
    user_id = models.ForeignKey(User)
    follower_id = models.ForeignKey(User)

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

