from django.db import models

# Create your models here.
from django.db import models
from users.models import User

class Mortuary(models.Model):
    mortuary_id = models.SmallIntegerField(primary_key=True)
    mortuary_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.mortuary_name

class MortuaryStaff(models.Model):
    staff_id = models.SmallIntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)
    mortuary_id = models.ForeignKey(Mortuary, on_delete=models.CASCADE)
    generated_code = models.CharField(max_length=30)

    def __str__(self):
        return f"Staff {self.staff_id} - {self.position}"

