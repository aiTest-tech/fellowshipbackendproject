from django.db import models
from base.models import BaseModel
import uuid


# Create your models here.
class MediaModel(BaseModel):  
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    title_eng = models.TextField()
    img = models.ImageField(upload_to='media/')
    title_guj = models.TextField()
    active_deactivate = models.BooleanField(default=False)


    def __str__(self):
        return self.title_eng
    

class BatchModel(BaseModel):
    batch = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.batch}"
    


class MeetOurFellowsModel(BaseModel):
    batch = models.ForeignKey(to=BatchModel, on_delete=models.CASCADE)
    department = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    ug_degree = models.CharField(max_length=255)
    age = models.IntegerField()
    post_graduation = models.CharField(max_length=255)
    pg_university = models.CharField(max_length=255)
    bachelore_degree = models.CharField(max_length=255)
    ug_university = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.batch}-{self.full_name}"
