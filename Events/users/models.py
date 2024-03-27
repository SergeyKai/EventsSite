from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    photo = models.ImageField(upload_to='users', default='user/user.png')
