from pathways.models import Pathway
from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Profile(models.Model):
    image = models.ImageField(
        verbose_name="profile picture", 
        default="default.jpeg", 
        upload_to="alumni_profile_pictures",
    )
    user = models.ForeignKey(
        User, null=False, blank=False, 
        on_delete=models.CASCADE
    )
    bio = models.TextField()
    pathway = models.ForeignKey(
        Pathway, null=False, blank=False, 
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{ self.user.username }'s profile info"
    def get_absolute_url(self):
        return reversed("home", args=[str(self.id)])
  
