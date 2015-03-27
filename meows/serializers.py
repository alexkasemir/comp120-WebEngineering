from rest_framework import serializers
from meows.models import User_Post
from meows.models import User

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = User_Post
		fields = ('image_URL', 'text_content', 'score', 'time_created', 'time_edited')
class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=False)
	class Meta:
		model = User
		fields = ('username', 'owner_email', 'password', 'active', 'member_since')
