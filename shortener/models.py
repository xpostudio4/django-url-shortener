import datetime

from django.conf import settings
from django.db import models

from .functions import base62_encode

class Link(models.Model):
    url = models.URLField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def get_url(self):
        return settings.SITE_BASE_URL + base62_encode(self.id)

    def __unicode__(self):
        return self.url

