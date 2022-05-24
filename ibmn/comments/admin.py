from django.contrib import admin
from ibmn.comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'news', 'pub_date', 'active')
    list_filter = ('active', 'pub_date')
    search_fields = ('name', 'email', 'content')
