from django.db import models
# import uuid

# Create your models here.
class Pathway(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=False, null=False)
    title = models.CharField(verbose_name="Alumni pathway", max_length=100, blank=False, null=False)
    description = models.CharField(
        max_length=250,
        verbose_name="pathway description", 
        default="Enter your pathway text",
        blank=False, null=False
    )
    def __str__(self) -> str:
        return f"{ self.title } pathway"
