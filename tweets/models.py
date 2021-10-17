from django.db import models
from django.conf import settings
import random

User = settings.AUTH_USER_MODEL

class TweetLike(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet       = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    timestamp   = models.DateTimeField(auto_now_add=True)

class Tweet(models.Model):
    # id        = models.AutoField(primary_key = True)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    # user        = models.ForeignKey(User, null= True, on_delete=models.SET_NULL) # tweets won't be deleted if user is deleted
    likes       = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    content     = models.TextField (blank = True, null =True)
    image       = models.FileField (blank = True, null =True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        
    def serialize (self):
        return {
            'id': self.id,
            'content': self.content,
            'likes': random.randint(0,100)
        }
