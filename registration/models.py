from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser

)

class User(AbstractBaseUser):
    username  = models.CharField(max_length = 100,unique = True)
    email = models.EmailField()
    USERNAME_FIELD = 'username'         #username

    def __str__(self):
        return self.username
