import uuid
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify 
from django.conf import settings
from ckeditor_uploader.fields import  RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from ibmn.categories.models import Subcategory
from ibmn.news.models import News
from ibmn.bignews.models import Bignews
from ibmn.trending.models import Trending






# Create your models here.

class Comment(MPTTModel):
    news = models.ForeignKey(News, null=True, on_delete=models.CASCADE, related_name='comments')
    bignews = models.ForeignKey(Bignews, null=True, on_delete=models.CASCADE, related_name='bignews_comments')
    trendnews = models.ForeignKey(Trending, null=True, on_delete=models.CASCADE, related_name='trendnews_comments')
    name = models.CharField(null=True,  blank = True, max_length=200 )
    email = models.EmailField(null=True,  blank = True, max_length=300)
    content = models.TextField(null=True,  blank = True)
    pub_date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ('-pub_date',)
    
    def __str__(self):
        return self.content


    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)
