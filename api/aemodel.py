from django.db import models
from api.models import VideoBlock, AudioBlock

class AudioElements(models.Model):
    id = models.AutoField(primary_key=True)
    video_block = models.OneToOneField(VideoBlock, null=True, blank=True, on_delete=models.CASCADE)
    audio_block = models.OneToOneField(AudioBlock, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.id