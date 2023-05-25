from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import VideoBlock, AudioBlock
from api.aemodel import AudioElements
from api.serializers import VideoBlockSerializer, AudioBlockSerializer
from rest_framework.generics import RetrieveAPIView
from api.serializers import AudioElementsSerializer

class VideoBlockViewSet(viewsets.ModelViewSet):
    queryset = VideoBlock.objects.all()
    serializer_class = VideoBlockSerializer

    def perform_create(self, serializer):
        duration = self.request.data.get('duration', {})
        serializer.save(duration_start_time=duration.get('start_time'),
                        duration_end_time=duration.get('end_time'))

    # Add type hint comment for request object
    def create(self, request: HttpRequest, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class AudioBlockViewSet(viewsets.ModelViewSet):
    queryset = AudioBlock.objects.all()
    serializer_class = AudioBlockSerializer

    def perform_create(self, serializer):
        duration = self.request.data.get('duration', {})
        serializer.save(duration_start_time=duration.get('start_time'),
                        duration_end_time=duration.get('end_time'))

    # Add type hint comment for request object
    def create(self, request: HttpRequest, *args, **kwargs):
        return super().create(request, *args, **kwargs)



class AudioElementsViewSet(RetrieveAPIView):
    
    queryset = AudioElements.objects.all()
    serializer_class = AudioElementsSerializer
    lookup_field = 'id'

    




