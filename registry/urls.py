# from django.contrib import admin
from django.urls import path
from . import views

# urlconfiguration
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('guestlist/', views.guestlists_list),
    path('guestlist_detail/<str:pk>/', views.guestlist_detail, name="guestlist_detail"),
    path('to_do/', views.to_do_list),
    path('to_do_detail/<str:pk>/', views.to_do_detail, name="to_do_detail"),
    # path('meal/', views.meal_selection),
    # path('recommendations/', views.music_recs),
    # path('upload/', views.upload),
    # path('hello/', views.say_hello)
]