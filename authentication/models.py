from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from rest_framework_jwt.settings import api_settings

# Our JWT payload
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# This variable handles the encoding of JWT tokens. By default, the HS256 encryption algorithm is used,
# which is HMAC with SHA-256 (Padilla, n.d.), which is necessary to meet the specification.
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
    Class to represent user model, Since we are creating your own User model we need to use AbstractBaseUser class.
    To make it easy to include Django's permission framework into your own user class, Django provides PermissionsMixin
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
        In this case, the property decorator makes it possible to access a token by calling `user.token` instead of
        `user.generate_jwt_token().` (Thinkster, 2021).
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Creates a JSON Web Token that is bound to this user's instance. 
        The method has an underscore prepended to show that the behavior is intended to be private (Bader, 2018), encouraging security through encapsulation.
        """
        payload = jwt_payload_handler(self)
        token = jwt_encode_handler(payload)

        return token


class Astronaut(User):
    """
    Creating custom Astronaut user model
    """
    objects = UserManager()
    age = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])


class AstronautHealthReport(models.Model):
    """
    Creating astronaut health report model
    """
    weight = models.FloatField(null=False, blank=False)
    blood_type = models.CharField(null=False, blank=False, max_length=10)
    blood_pressure = models.FloatField(null=False, blank=False)
    heart_rate = models.FloatField(null=False, blank=False)
    muscle_mass = models.FloatField(null=False, blank=False)
    feedback = models.TextField(
        null=True, blank=True, default='No feedback as of yet')
    astronaut = models.ForeignKey(Astronaut, on_delete=models.CASCADE)

    def __str__(self):
        return self.astronaut.username


class Scientist(User):
    """
    Creating scientist model
    """
    objects = UserManager()
    specialty = models.CharField(null=False, blank=False, max_length=100)


# References
# Bader, D. (2018) The Meaning of Underscores in Python. Available from: https://dbader.org/blog/meaning-of-underscores-in-python [Accessed 25 October 2021].
# Padilla, J. (n.d.) REST framework JWT Auth. Available from: https: // jpadilla.github.io/django-rest-framework-jwt/ [Accessed 23 October 2021].
# Thinkster. (2021) Setting up JWT Authentication. Available from: https://thinkster.io/tutorials/django-json-api/authentication [Accessed 25 October 2021].
