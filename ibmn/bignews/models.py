import uuid
from  PIL import Image
from datetime import datetime
from django.core.validators import MinLengthValidator
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify 
from django.conf import settings
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
from taggit.managers import TaggableManager
from hitcount.models import HitCountMixin, HitCount
#from imagekit.models import ProcessedImageField
#from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import  RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from ibmn.categories.models import Category



# Create your models here.

class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    # tag = models.ForeignKey(Tag, related_name="uuid_tagged_items", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")

class Bignews(models.Model, HitCountMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    title = models.CharField(null=True,  blank = True, max_length=200 )
    short_txt = models.CharField(null=True,  blank = True,  max_length=200)
    body_txt = RichTextUploadingField(null=True,  blank = True)
    pub_date = models.DateTimeField(null=True,)
    slug = models.SlugField(null=True, unique=True)
    image = models.ImageField(upload_to='profile_image', null=True)         
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='bignews_categories', null=True, blank=True)
    tags = TaggableManager(through=UUIDTaggedItem)
    hit_count_generic = GenericRelation(HitCount, object_id_field = 'object_pk', related_query_name='hit_count_generic_relation')


    class Meta:
        ordering = ['-pub_date']

      
    def get_absolute_url(self):
        return reverse('bignews:bignews_detail', kwargs={'slug': self.slug})
      
         
    def get_comments(self):
        return self.bignews_comments.filter(parent=None).filter(active=True)

    
    def save(self, *args, **kwargs):
        self.pub_date = datetime.now()
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

        if self.pub_date is None:
            self.pub_date = datetime.now()
            self.save()
        if self.slug is None:
            self.slug = slugify(self.title)
            self.save()

        if self.image:
            img = Image.open(self.image.path)

            if img.height > 552 or img.width > 770:
                new_height = 552
                new_width = 770
                img = img.resize((new_width, new_height))
                img.save(self.image.path)    

    def __str__(self):
        return self.title