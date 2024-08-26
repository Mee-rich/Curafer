from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserProfileManager
from django.utils.translation import gettext_lazy as _


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), max_length=60, unique=True)
    username = models.CharField(max_length=60, default=None)
    # first_name = models.CharField(max_length=60, default=None)
    # last_name = models.CharField(max_length=60, default=None)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        """ Return string represention of our user """
        return self.email
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin