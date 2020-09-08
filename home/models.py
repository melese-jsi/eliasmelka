from django.db import models

# Create your models here.
from django.db.models import Model


class Music(Model):
    title = models.CharField(max_length=255,)
    picture = models.ImageField(upload_to='album_arts/')
    release_year = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    artist = models.CharField(max_length=100)
    youtube_link_1 = models.URLField(max_length=300, blank=True)
    youtube_link_2 = models.URLField(max_length=300, blank=True)
    youtube_link_3 = models.URLField(max_length=300, blank=True)
    youtube_link_4 = models.URLField(max_length=300, blank=True)
    youtube_link_5 = models.URLField(max_length=300, blank=True)
    is_album = models.BooleanField(default=True)
    is_sound_track = models.BooleanField(default=False)
    is_community_work = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    def getComments(self):
        return self.comment_set.all()
    def getLinks(self):
        links = []
        if not self.youtube_link_1 == '':
            links.append(self.youtube_link_1)
        if not self.youtube_link_2 == '':
            links.append(self.youtube_link_2)
        if not self.youtube_link_3 == '':
            links.append(self.youtube_link_3)
        if not self.youtube_link_4 == '':
            links.append(self.youtube_link_4)
        if not self.youtube_link_5 == '':
            links.append(self.youtube_link_5)
        return links




