from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 25, unique= true)
    owner_email = models.EmailField(max_length = 50, unique= true)
    password = models.CharField(max_length = 50)
    icon_URL = models.FilePathField(path = "")
    active = models.BooleanField()
    member_since = models.DateField
    def __str__(self):
        return self.username


