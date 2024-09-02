from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    user_id = models.SmallIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

