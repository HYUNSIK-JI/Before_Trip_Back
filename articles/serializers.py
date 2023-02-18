from rest_framework import serializers
from .models import Articles

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.email')
    class Meta:
        model = Articles
        fields = ("id", "title", "content", "created_at", "updated_at", "user")