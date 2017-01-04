from django.conf import settings
from django.db import models
from tags.models import Tag


class BlogEntry(models.Model):
    title = models.CharField(max_length=160)
    body = models.TextField()
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
