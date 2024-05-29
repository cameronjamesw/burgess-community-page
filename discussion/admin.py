from django.contrib import admin
from .models import Discussion, Comment

# Register your models here.

admin.site.register(Discussion)
admin.site.register(Comment)