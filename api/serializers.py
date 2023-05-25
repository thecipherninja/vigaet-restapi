from rest_framework import serializers
from api.models import VideoBlock, AudioBlock
from api.aemodel import AudioElements


class VideoBlockSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()

    class Meta:
        model = VideoBlock
        fields = ['id', 'type', 'audio_id', 'url', 'duration']

    def get_duration(self, obj):
        return {
            'start_time': obj.duration_start_time,
            'end_time': obj.duration_end_time
        }

    def create(self, validated_data):
        duration_data = validated_data.pop('duration', {})
        start_time = duration_data.get('start_time')
        end_time = duration_data.get('end_time')
        instance = super().create(validated_data)

        if start_time is not None:
            instance.duration_start_time = start_time
        if end_time is not None:
            instance.duration_end_time = end_time
        instance.save()

        return instance





class AudioBlockSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()

    class Meta:
        model = AudioBlock
        fields = ['id', 'type', 'video_component_id', 'high_volume', 'low_volume', 'duration', 'url']

    def get_duration(self, obj):
        return {
            'start_time': obj.duration_start_time,
            'end_time': obj.duration_end_time
        }

    def create(self, validated_data):
        duration_data = validated_data.pop('duration', {})
        start_time = duration_data.get('start_time')
        end_time = duration_data.get('end_time')
        instance = super().create(validated_data)

        if start_time is not None:
            instance.duration_start_time = start_time
        if end_time is not None:
            instance.duration_end_time = end_time
        instance.save()

        return instance


class AudioElementsSerializer(serializers.ModelSerializer):
    video_blocks = VideoBlockSerializer(source='video_block', read_only=True)
    audio_blocks = AudioBlockSerializer(source='audio_block', read_only=True)

    class Meta:
        model = AudioElements
        fields = ['id', 'video_blocks', 'audio_blocks']
