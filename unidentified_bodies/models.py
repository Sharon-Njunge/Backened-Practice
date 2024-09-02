from django.db import models

# Create your models here.
from django.db import models
from mortuary.models import MortuaryStaff

class UnidentifiedBody(models.Model):
    body_id = models.SmallIntegerField(primary_key=True)
    mortuaryStaff_id = models.ForeignKey(MortuaryStaff, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    skin_color = models.CharField(max_length=50)
    weight = models.FloatField()
    height = models.FloatField()
    body_marks = models.TextField()
    reporting_date = models.DateTimeField()
    clothes_worn = models.TextField()
    hair_color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

