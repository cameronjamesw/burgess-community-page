from django.db import models
from django.contrib.auth.models import User 

STATUS = ((0, "Draft"), (1, "Published"))
# Create your models here.

class Discussion(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="discussion_post"
    )
    content = models.TextField
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
