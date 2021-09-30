from django.contrib import admin
from .models import User, Astronaut,Scientist

# Register your models here.
admin.site.register(User)
admin.site.register(Astronaut)
admin.site.register(Scientist)
