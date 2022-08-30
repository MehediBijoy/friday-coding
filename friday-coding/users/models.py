from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, name, email, phone_number, password=None):
        if not email:
            raise ValueError('user must have an email address')

        if not name:
            raise ValueError('user must have an name')

        user = self.model(
            name=name,
            phone_number=phone_number,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, name, email, phone_number, password=None):
        user = self.create_user(
            name=name,
            phone_number=phone_number,
            email=self.normalize_email(email),
            password=password
        )

        user.is_admin = True
        user.is_superadmin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50, unique=True, null=False)
    phone_number = models.CharField(max_length=15, unique=True, null=False)

    # django user required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']

    objects = UserManager()

    def __str__(self) -> str:
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(slef, add_label):
        return True

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
