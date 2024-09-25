from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Discussion, Comment

# Register your models here.

@admin.register(Discussion)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'excerpt', 'slug', 'status',)
    search_fields = ['title']
    list_filter = ('status', 'approved',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Comment)