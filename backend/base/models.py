from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password, check_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, email=None, **extra_fields):
        """Метод для создания обычного пользователя"""
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, email=None, **extra_fields):
        """Метод для создания суперпользователя"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, email, **extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=80, unique=True)
    email = models.EmailField(_('email address'), unique=True, blank=True, null=True)
    password = models.CharField(max_length=120)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def set_password(self, raw_password):
        """Метод для хеширования пароля"""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Метод для проверки пароля"""
        return check_password(raw_password, self.password)

    def has_module_perms(self, app_label):
        """Метод для проверки разрешений на доступ к модулям"""
        return True  # Вернуть True или реализовать логику проверки

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
