from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Post
        fields = (
            'id', 
            'title', 
            'image', 
            'publish_date', 
            'update_date', 
            'content', 
            'author', 
            'comment_count', 
            'view_count', 
            'like_count',
            )