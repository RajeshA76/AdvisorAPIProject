from django.db import models


# Create your models here.
class AdvisorModel(models.Model):

    advisor_id = models.AutoField(primary_key=True)
    AdvisorName = models.CharField(max_length=100,unique=True,blank=False)
    AdvisorPhotoUrl = models.URLField(max_length=255)