from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    employee_code = models.PositiveIntegerField(default=0)

    def full_name(self):
        if self.first_name:
            return self.first_name + " " + self.last_name
        else:
            return self.username