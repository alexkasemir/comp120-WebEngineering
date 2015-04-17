from django import forms
from meows.models import User_Post


class UserPostForm(forms.ModelForm):
    class Meta:
        model = User_Post

        fields = ["image_URL", "text_content"]
