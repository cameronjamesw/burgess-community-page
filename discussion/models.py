from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
# Create your models here.

# This is the Discussion Model


class Discussion(models.Model):
    """
    This model stores a single discussion entry, related to :model:`auth.user`.
    """
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="discussion_post"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | Written by {self.author}"

# This is the Comment Model


class Comment(models.Model):
    """
    This model creates a singular comment which is attached
    to a discussion, related to :model:`auth.User` and
    :model:`discussion.Discussion`.
    """
    discussion = models.ForeignKey(
        Discussion, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
