from django.urls import path
from . import views

# urlconfiguration
urlpatterns = [
    path('hello/', views.say_hello),
    # path(r'^rsvp/$', views.rsvp),
    # path(r'^$',),
    # path(r'^registry$', views.gift_registry),
    # path(r'^meal$', views.meal_selection),
    # path(r'^recommendations$', views.music_recs),
    # path(r'^upload$', views.upload),
    # path(r'^todo$', views.todo)
]