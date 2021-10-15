from django.db import models
from django.conf import settings
import random

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    # id        = models.AutoField(primary_key = True)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    # user        = models.ForeignKey(User, null= True, on_delete=models.SET_NULL) # tweets won't be deleted if user is deleted
    content     = models.TextField (blank = True, null =True)
    image       = models.FileField (blank = True, null =True)

    class Meta:
        ordering = ['-id']
        
    def serialize (self):
        return {
            'id': self.id,
            'content': self.content,
            'likes': random.randint(0,100)
        }
