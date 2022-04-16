from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class CustomUserManager(BaseUserManager):

    def create_user(self, email, username,  password=None):
        if not email:
            raise ValueError('Users must have an email address!')
        if not username:
            raise ValueError('Users must have a username!')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):

        user = self.create_user(
            email,
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
        db_index=True
    )
    username = models.CharField(max_length=55)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    posts = models.ManyToManyField('post.Post', related_name='posts')
    favorites = models.ManyToManyField('post.Post', related_name='favorites', null=True, blank=True)
    avatar = models.ImageField(upload_to='profile_images', default='profile.png')

    def __str__(self):
        return self.owner.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
