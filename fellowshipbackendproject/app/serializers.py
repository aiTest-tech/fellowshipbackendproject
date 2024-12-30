from rest_framework import serializers
from .models import MediaModel, MeetOurFellowsModel, BatchModel


class MediaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaModel
        fields = "__all__"


class MeetOurFellowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetOurFellowsModel
        fields = "__all__"

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchModel
        fields = "__all__"