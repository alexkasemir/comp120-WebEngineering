from django.contrib import admin
from meows.models import User, User_Post, Friends, Posts, Comment, Album, Albums, Feedback

# Register your models here.
admin.site.register(User)
admin.site.register(User_Post)
admin.site.register(Friends)
admin.site.register(Posts)