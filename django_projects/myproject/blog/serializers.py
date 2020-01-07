
from . models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    """
    Serializer for model Tasks
    """
    class Meta:
        model = Blog
        fields = ('id', 'name', 'tagline')
    