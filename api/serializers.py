from rest_framework import serializers
from .models import VideoElement, AudioElement, AudioFragments

class VideoElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoElement
        fields = '__all__'
