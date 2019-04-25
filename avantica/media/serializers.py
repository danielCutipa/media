from rest_framework import serializers

from avantica.media.models import Media, Timer

class MediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('id', 'url')

class TimerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = ('id', 'init_date', 'end_date', 'media_id')