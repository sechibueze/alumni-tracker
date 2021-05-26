from django.db import models

# Create your models here.

class Profile(models.Model):
    bio = models.TextField()
    # lastname = models.CharField(max_length=20)
    # email = models.EmailField()
    # password = models.CharField(max_length=20)
    # profile = models.ForeignKey(Profile)
