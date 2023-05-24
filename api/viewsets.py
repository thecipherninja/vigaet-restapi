from rest_framework import viewsets
from . import models
from . import serializers

class VideoElementViewset(viewsets.ModelViewSet):
    queryset = models.VideoElement.objects.all()
    serializer_class = serializers.VideoElementSerializer
