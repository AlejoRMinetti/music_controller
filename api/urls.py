# urls local to this ap
from django.urls import path
from .views import main # . for import relative to this code

urlpatterns = [
    path('home',main), # urls from base url in music_controller urls.py
    path('',main) 
]
