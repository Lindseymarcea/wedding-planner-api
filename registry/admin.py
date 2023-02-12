from django.contrib import admin
from .models import Guestlist, To_do, Cuisine, Song_choice, Gift

# Register your models here.
admin.site.register(Guestlist),
admin.site.register(Cuisine),
admin.site.register(To_do),
admin.site.register(Song_choice)
admin.site.register(Gift)
