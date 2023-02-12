from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, verbose_name='Пользователь')
    bio = models.CharField(max_length=150, verbose_name='Биография')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [        'username',]

    def __str__(self):
        return self.username

    class Model:
        verbose_name = 'Пользователь'