import uuid
from datetime import datetime
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse
from django.template.defaultfilters import slugify 
from django.conf import settings
from hitcount.models import HitCountMixin, HitCount
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import  RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from ibmn.categories.models import Subcategory



# Create your models here.

class News(models.Model, HitCountMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    title = models.CharField(null=True,  blank = True, max_length=200 )
    short_txt = models.CharField(null=True,  blank = True, max_length=60, validators=[MinLengthValidator(58)])
    body_txt = RichTextUploadingField(null=True,  blank = True)
    pub_date = models.DateTimeField(null=True,)
    slug = models.SlugField(null=True, unique=True, default='ibmn_news')
    image = ProcessedImageField(upload_to='profile_image',processors=[ResizeToFill(612, 408)],
                                           format='JPEG',
                                           options={'quality': 60})         
    category = models.ForeignKey('categories.Subcategory', on_delete=models.CASCADE, related_name='categories', null=True, blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field = 'object_pk', related_query_name='hit_count_generic_relation')



    class Meta:
        ordering = ['-pub_date']


    def get_absolute_url(self):
        return reverse('news:news_detail', kwargs={'slug': self.slug})
        
    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)



    def save(self, *args, **kwargs):
        if self.pub_date is None:
            self.pub_date = datetime.now()
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
        
    def __str__(self):
        return self.title