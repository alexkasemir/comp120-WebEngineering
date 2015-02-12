from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 25, unique= True)
    owner_email = models.EmailField(max_length = 50, unique= True)
    password = models.CharField(max_length = 50)
    icon_URL = models.ImageField()
    active = models.BooleanField(default = True)
    member_since = models.DateField(auto_now_add = True)
    def __str__(self):
        return self.username

class User_Post(models.Model):
    contains_image = models.BooleanField(default = False)
    image_URL = models.ImageField()
    text_content = models.TextField(max_length = 255)
    score = models.IntegerField()
    time_created = models.DateField(auto_now_add = True)
    time_edited = models.DateField(auto_now = True)
    active = models.BooleanField(default = True)

    @classmethod
    def create(text_cont):
        user_post = User_Post(text_content=text_cont)
        return user_post

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

