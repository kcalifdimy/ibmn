import uuid
from datetime import datetime
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify 
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import  RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from ibmn.categories.models import Category



# Create your models here.

class Trending(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    title = models.CharField(null=True,  blank = True, max_length=200 )
    short_txt = models.CharField(null=True,  blank = True,  max_length=200)
    body_txt = RichTextUploadingField(null=True,  blank = True)
    pub_date =  models.DateTimeField(null=True,)
    slug = models.SlugField(null=True, unique=True, default='ibmn')
    image = ProcessedImageField(upload_to='profile_image',processors=[ResizeToFill(668, 455)],
                                           format='JPEG',
                                           options={'quality': 100})
     
    category_name = models.ForeignKey('categories.Category', on_delete=models.CASCADE, null=True, blank=True)


    def get_absolute_url(self):
        return reverse('trending:trendnews_detail', kwargs={'slug': self.slug})




    class Meta:
        ordering = ['-pub_date']

    def save(self, *args, **kwargs):
        if self.pub_date is None:
            self.pub_date = datetime.now()
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_comments(self):
        return self.trendnews_comments.filter(parent=None).filter(active=True)


        
    def __str__(self):
        return self.title