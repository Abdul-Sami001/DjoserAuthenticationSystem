from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, name, is_admin=False, password=None):
        if not email:
            raise ValueError("You must provide an email address")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            is_admin=is_admin,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, is_admin=True, password=None):
        if not email:
            raise ValueError("You must provide an email address")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            is_admin=is_admin,
        )
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email", max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "name",
        "is_admin",
    ]  # Corrected typo: 'REQUIRED_FIELDS' instead of 'REQUIRED_FIELD'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
