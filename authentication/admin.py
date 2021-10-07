from django.contrib import admin
from .models import User, Astronaut, Scientist, AstronautHealthReport

# Register your models here.
admin.site.register(User)
admin.site.register(Astronaut)
admin.site.register(Scientist)
admin.site.register(AstronautHealthReport)
