import uuid
from  embed_video.fields  import  EmbedVideoField
from datetime import datetime
from django.db import models
#Create your models here.

class Bignews(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(null=True,  blank = True, max_length=100 )
    pub_date =  models.DateTimeField(null=True,)
    video_url = EmbedVideoField()


    class Meta:
        ordering = ['-pub_date']

        
    def save(self, *args, **kwargs):
        if self.pub_date is None:
            self.pub_date = datetime.now()

        return super().save(*args, **kwargs)


    def __str__(self):
        return self.title
    