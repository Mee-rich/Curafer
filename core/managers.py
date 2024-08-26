from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserProfileManager(BaseUserManager):
    """ Manager for user profiles """
    def create_user(self, email, username, password, **extra_fields):
            """ Create a new user profile """
            if not email:
                raise ValueError('User must have an email address')

            email = self.normalize_email(email)
            user = self.model(email=email, username=username, **extra_fields)

            user.set_password(password)
            user.save(using=self._db)

            return user

    def create_superuser(self, email, username, password):
        """ Create a new superuser profile """
        
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.is_superuser =True
        user.save(using=self._db)
        return user