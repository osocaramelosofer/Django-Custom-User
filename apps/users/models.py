from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self, username, email, names, surnames, password, is_admin, **extra_fields):
        if not email:
            raise ValueError('You need an email')

        user = self.model(
            username=username,
            email = self.normalize_email(email),
            names=names,
            surnames=surnames,
            is_admin=is_admin,
            **extra_fields
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, names, surnames, password, **extra_fields):
        return self._create_user(username, email, names, surnames, password, False, **extra_fields)

    def create_superuser(self, username, email, names, surnames, password, **extra_fields):
        return self._create_user(username, email, names, surnames, password, True, **extra_fields)

class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=30)
    email = models.EmailField('Email', max_length=50, unique=True)
    names = models.CharField('Names', max_length=100, blank=True, null=True)
    surnames = models.CharField('Surnames', max_length=100, blank=True, null=True)
    image = models.ImageField('Profile picture', upload_to='profile/', max_length=200, blank=True, null=True)
    active_user = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'names', 'surnames']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'User: {self.names} {self.surnames}'
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    


