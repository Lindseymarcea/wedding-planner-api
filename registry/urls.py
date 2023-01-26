from django.urls import path
from . import views

# urlconfiguration
urlpatterns = [
    path('hello/', views.say_hello)
]