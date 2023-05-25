from django.db import models

class VideoBlock(models.Model):
    id = models.AutoField(max_length=50, primary_key=True)
    type = models.CharField(max_length=50)
    audio_id = models.CharField(max_length=50)
    url = models.URLField()
    duration_start_time = models.PositiveIntegerField()
    duration_end_time = models.PositiveIntegerField()

    def __str__(self):
        return self.id

class AudioBlock(models.Model):
    id = models.AutoField(max_length=50, primary_key=True)
    type = models.CharField(max_length=50)
    video_component_id = models.CharField(max_length=50, null=True)
    high_volume = models.IntegerField()
    low_volume = models.IntegerField()
    duration_start_time = models.PositiveIntegerField()
    duration_end_time = models.PositiveIntegerField()
    url = models.URLField(null=True)

    def __str__(self):
        return self.id


