# music_player_app/urls.py

from django.urls import path
from .views import index, download_midi

urlpatterns = [
    path("", index, name="index"),
    path("download_midi/", download_midi, name="download_midi"),
]
