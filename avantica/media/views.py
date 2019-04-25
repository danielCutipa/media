# from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from avantica.media.models import Media, Timer
from avantica.media.serializers import MediaSerializers, TimerSerializers

class MediaViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializers

class TimerViewSet(ModelViewSet):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializers
    