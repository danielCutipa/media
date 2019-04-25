from django.db import models
from avantica.media.mixins import TimeStampModel

class Media(TimeStampModel):
    url = models.CharField(max_length=200)

class Timer(TimeStampModel):
    init_date = models.DateTimeField()
    end_date = models.DateTimeField()
    media = models.ForeignKey(Media, on_delete=models.CASCADE)