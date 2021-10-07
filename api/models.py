from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class Astronaut(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    percent_field = models.PositiveIntegerField(validators=[MaxValueValidator(100), ])


