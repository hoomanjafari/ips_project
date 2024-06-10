from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import MyUserManager


class MyUser(AbstractUser):
    username = models.CharField(max_length=66, unique=True, verbose_name=_('نام'))
    mobile = models.CharField(max_length=33, unique=True, verbose_name=_('شماره تماس'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('mobile',)

    def __str__(self):
        return f'( {self.username} ) -- ( {self.mobile} ) -- ( {self.created} )'
