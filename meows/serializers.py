from rest_framework import serializers
from meows.models import User_Post

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = User_Post
		fields = ('image_URL', 'text_content', 'score', 'time_created', 'time_edited')
