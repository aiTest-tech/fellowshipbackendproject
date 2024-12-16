from rest_framework import serializers
from .models import MediaModel


class MediaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaModel
        fields = "__all__"  # Or specify fields as a list, e.g., ['id', 'img', 'title']
