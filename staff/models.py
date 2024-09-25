from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User


# This refers to which camp the user works at
CAMPS = ((0, "Burgess"), (1, "Hayward"))

# Create your models here.

# This model refers to the Staff Members


class Staff_Member(models.Model):
    """
    This model stores a singular staff profile, related to :model:`auth.User`.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    photo = CloudinaryField("image", default="placeholder")

    # Camp refers to which camp they are working at, Burgess or Hayward
    camp = models.IntegerField(choices=CAMPS, default=0)
    position = models.CharField(max_length=50)

    # Tenure refers to how longer they have been employed by the camp
    tenure = models.IntegerField(default=0)
    facts = models.TextField(blank=False)
    memory = models.TextField(blank=False)
    approved = models.BooleanField(default=False)
