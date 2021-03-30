from rest_framework import serializers
from .models import Upload
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Upload
        fields='__all__'