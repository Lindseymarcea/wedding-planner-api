# from django.contrib import admin
from django.urls import path
from . import views

# urlconfiguration
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('guestlist/', views.guestlists_list),
    path('guestlist_detail/<str:pk>/', views.guestlist_detail, name="guestlist_detail"),
    # path(r'^rsvp/$', views.rsvp),
    # path(r'^$',),
    # path(r'^registry$', views.gift_registry),
    # path(r'^meal$', views.meal_selection),
    # path(r'^recommendations$', views.music_recs),
    # path(r'^upload$', views.upload),
    # path(r'^todo$', views.todo)
    path('hello/', views.say_hello)
]