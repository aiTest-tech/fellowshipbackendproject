from django.db import models
from base.models import BaseModel


# Create your models here.
class MediaModel(BaseModel):
    # img = models.ImageField(upload_to="media/")
    # title = models.TextField()
    # active    
    title_eng = models.TextField()
    img = models.ImageField(upload_to='media/')
    title_guj = models.TextField()
    active_deactivate = models.BooleanField(default=False)


    def __str__(self):
        return self.title_eng