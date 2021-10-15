from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from rest_framework_jwt.settings import api_settings

# Our JWT payload
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`.
    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, email, password=None, first_name=None,
                    last_name=None):
        """
        Create and return a `User` with an email, username, first_name, last_name
        and password.
        """
        if username is None:
            raise TypeError("Users must have a username")
        if email is None:
            raise TypeError("Users must have an email address")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_staff=False,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password=None, first_name=None, last_name=None):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if username is None:
            raise TypeError("Super users must have a username")
        if email is None:
            raise TypeError("Super must have an email address")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_superuser=True,
            is_staff=True,
        )
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Class to represent user model
    """
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.
        This string is used when a `User` is printed in the console.
        """
        return self.username

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().
        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's instance and has an expiry
        date set to 60 days into the future.
        """
        payload = jwt_payload_handler(self)
        token = jwt_encode_handler(payload)

        return token


class Astronaut(User):
    objects = UserManager()
    age = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])


class AstronautHealthReport(models.Model):
    weight = models.FloatField(null=False, blank=False)
    blood_type = models.CharField(null=False, blank=False, max_length=10)
    blood_pressure = models.FloatField(null=False, blank=False)
    heart_rate = models.FloatField(null=False, blank=False)
    muscle_mass = models.FloatField(null=False, blank=False)
    astronaut = models.ForeignKey(Astronaut, on_delete=models.CASCADE)

    def __str__(self):
        return self.astronaut.username


class Scientist(User):
    objects = UserManager()
    specialty = models.CharField(null=False, blank=False, max_length=100)


class HealthReportFeedBack(models.Model):
    recommendation = models.TextField(null=True, blank=True)
    scientist = models.ForeignKey(Scientist, on_delete=models.CASCADE)
    astronaut = models.ForeignKey(Astronaut, on_delete=models.CASCADE)

    def __str__(self):
        return self.recommendation
