from django.contrib import admin
from .models import Play
from .models import Character
from .models import Todo
from .models import Tracker

# Register your models here.
admin.site.register(Play)
admin.site.register(Character)
admin.site.register(Todo)
admin.site.register(Tracker)
