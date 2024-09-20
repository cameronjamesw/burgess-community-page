from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

CAMPS = ((0, "Burgess"), (1, "Hayward"))
# Create your models here.

class Staff_Member(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    photo = CloudinaryField("image", default="placeholder")
    camp = models.IntegerField(choices=CAMPS, default=0)
    position = models.CharField(max_length=50)
    tenure = models.IntegerField(default=0)
    facts = models.TextField(blank=False)
    memory = models.TextField(blank=False)