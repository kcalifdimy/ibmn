import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.

class Breaking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=300, default='text')
    image = ProcessedImageField(upload_to='profile_image',processors=[ResizeToFill(12, 10)],
                                           format='JPEG',
                                           options={'quality': 60})         
   
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.text


