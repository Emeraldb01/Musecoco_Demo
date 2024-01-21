from . import views, generation
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('download/', generation.user_text_input, name='user_text_input'),
    path("download_midi/", views.download_midi, name="download_midi"),
]