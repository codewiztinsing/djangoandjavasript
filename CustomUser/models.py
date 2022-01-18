from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_coordinator = models.BooleanField(default=False)
    is_trainee     = models.BooleanField(default = True)
  