from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email

class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, signup=None, **extra_fields,):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        try:
            validate_email(email)
        except:
            raise ValueError('Users must have a valid email address')
        else:
            email = self.normalize_email(email)

        if signup:
            password_number = any(char.isdigit() for char in password)
            if not password_number:
                raise ValueError('Password must contain a number')

            password_length = True if len(password) > 6 else False
            if not password_length:
                raise ValueError('Password must be at least 6 characters')

            password_uppercase = (any(char.isupper() for char in password))

            if password_uppercase:
                raise ValueError('Password must contain an uppercase character')
            else:
                pass

        user = self.model(
            email = email,
            **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email = email, password=password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user