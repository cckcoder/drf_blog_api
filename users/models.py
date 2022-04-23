# users/models.py

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model( email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'), unique=True, blank=True,
                              null=True)
    emp_id = models.IntegerField(help_text="เลขประจำตัว", unique=True)
    department = models.CharField(max_length=45,help_text="สายงาน")
    first_name = models.CharField(max_length=45, blank=True)
    last_name = models.CharField(max_length=45, blank=True)
    position = models.CharField(max_length=45, blank=True)
    zone = models.CharField(max_length=45, blank=True, help_text="เขต")
    sub_position = models.CharField(max_length=45, blank=True, help_text="สังกัดย่อ")

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'emp_id'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.emp_id)
