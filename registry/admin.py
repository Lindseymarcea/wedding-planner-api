from django.contrib import admin
from .models import Guestlist, To_do, Cuisine
# , Meal, Gift, Song_choice

# Register your models here.
admin.site.register(Guestlist),
admin.site.register(Cuisine),
admin.site.register(To_do)
# admin.site.register(Gift)
# admin.site.register(Meal)
