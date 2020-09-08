from django.conf import settings
from django.db import models

# Create your models here.
from django.utils.timezone import now

from home.models import Music


class Comment(models.Model):
    body = models.TextField(max_length=300)
    created_time= models.DateTimeField(default=now)
    last_mod_time = models.DateTimeField(default=now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    music = models.ForeignKey(Music,on_delete=models.CASCADE)
