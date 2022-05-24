from unicodedata import category
from django.contrib import admin
from ibmn.categories.models import Subcategory, Category
from mptt.admin import MPTTModelAdmin


admin.site.register(Subcategory , MPTTModelAdmin) 

admin.site.register(Category ) 