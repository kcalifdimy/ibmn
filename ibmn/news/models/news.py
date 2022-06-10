import uuid
from datetime import datetime
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse
from django.template.defaultfilters import slugify 
from django.conf import settings
from taggit.managers import TaggableManager
from hitcount.models import HitCountMixin, HitCount
#from imagekit.models import ProcessedImageField
#from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import  RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
from ibmn.categories.models import Subcategory


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    # tag = models.ForeignKey(Tag, related_name="uuid_tagged_items", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")


# Create your models here.

class News(models.Model, HitCountMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    title = models.CharField(null=True,  blank = True, max_length=200 )
    short_txt = models.CharField(null=True,  blank = True, max_length=200, validators=[MinLengthValidator(60)])
    body_txt = RichTextUploadingField(null=True,  blank = True)
    pub_date = models.DateTimeField(null=True,)
    slug = models.SlugField(null=True, unique=True, default='ibmn_news')
    #image = models.ImageField(upload_to='profile_image')
    image = models.ImageField(upload_to='profile_image', null=True)         
    category = models.ForeignKey('categories.Subcategory', on_delete=models.CASCADE, related_name='categories', null=True, blank=True)
    tags = TaggableManager(through=UUIDTaggedItem)
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