from rest_framework import serializers
from .models import Articles, Comment

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.email')
    class Meta:
        model = Articles
        fields = ("id", "title", "content", "created_at", "updated_at", "user")

class CommentSerializer(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source = 'user.email')
    ariticles = serializers.ReadOnlyField(source = "articles.pk")
    
    class Meta:
        model = Comment
        fields = ("id", "ariticles", "content", "created_at", "updated_at", "user")