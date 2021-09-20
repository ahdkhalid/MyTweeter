from django.db import models
import random
# Create your models here.
class Tweet(models.Model):
    # id        = models.AutoField(primary_key = True)
    content     = models.TextField (blank = True, null =True)
    image     = models.FileField (blank = True, null =True)

    class Meta:
        ordering = ['-id']
        
    def serialize (self):
        return {
            'id': self.id,
            'content': self.content,
            'likes': random.randint(0,100)
        }
