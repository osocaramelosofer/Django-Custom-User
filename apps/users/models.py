from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, names, surnames, password=None):
        if not email:
            raise ValueError('You need an email')

        user = self.model(
            username=username,
            email = self.normalize_email(email),
            names=names,
            surnames=surnames
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(username, email, names, surnames, password):
        user = self.create_user(
            email,
            username=username,
            names=names,
            surnames=surnames
        )
        user.admin_user = True
        user.save()
        return user

class User(AbstractBaseUser):
    username = models.CharField('User name', unique=True, max_length=30)
    email = models.EmailField('Email', max_length=50, unique=True)
    names = models.CharField('Names', max_length=100, blank=True, null=True)
    surnames = models.CharField('Surnames', max_length=100, blank=True, null=True)
    image = models.ImageField('Profile picture', upload_to='profile/', max_length=200, blank=True, null=True)
    active_user = models.BooleanField(default=True)
    admin_user = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'names', 'surnames']

    def __str__(self):
        return f'User: {self.names} {self.surnames}'
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.admin_user

    


