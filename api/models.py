from django.db import models

# Create your models here.

class AudioElement(models.Model):
    AUDIO_TYPES = (
        ('vo', 'Voice Over'),
        ('bg_music', 'Background Music'),
        ('video_music', 'Video Music'),
    )

    id = models.CharField(max_length=255, primary_key=True)
    type = models.CharField(max_length=20, choices=AUDIO_TYPES)
    video_component_id = models.CharField(max_length=255, null=True, blank=True)
    high_volume = models.IntegerField()
    low_volume = models.IntegerField()
    duration_start_time = models.IntegerField(null=True, blank=True)
    duration_end_time = models.IntegerField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

class VideoElement(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    type = models.CharField(max_length=20)
    audio_id = models.CharField(max_length=255)
    url = models.URLField()
    duration_start_time = models.FloatField()
    duration_end_time = models.FloatField()

class AudioFragments(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    url = models.URLField(null=True, blank=True)
    type = models.CharField(max_length=20)
    volume = models.IntegerField()
    duration_start_time = models.FloatField()
    duration_end_time = models.FloatField()

