from django.contrib import admin
from .models import Discussion, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Discussion)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status',)
    search_fields = ['title']
    list_filter = ('status', 'approved',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Comment)