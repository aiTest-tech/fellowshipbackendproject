from django.db import models
from base.models import BaseModel


# Create your models here.
class MediaModel(BaseModel):
    img = models.ImageField(upload_to="media/")
    title = models.TextField()
