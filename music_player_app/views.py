from django.shortcuts import render
from django.http import HttpResponse
import mimetypes
import os


def print_input(request):
    user_input = ""

    if request.method == "POST":
        user_input = request.POST.get("user_input", "")
        print(f"User typed: {user_input}")

    return user_input


def play_sample(request):
    audio_file_path = "static/music/abc.mp3"
    return audio_file_path


def download_midi(request):
    # Specify the file path on the server
    file_path = "/Users/emeraldchang/Desktop/Music_generation/demo_site/Musecoco_Demo/music_player_app/static/music/abc.mp3"

    # Open the file and create an HttpResponse object
    with open(file_path, "rb") as file:
        response = HttpResponse(
            file.read(), content_type=mimetypes.guess_type(file_path)[0]
        )
        # Set the Content-Disposition header to prompt the user for download
        response[
            "Content-Disposition"
        ] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response


def index(request):
    user_input = print_input(request)
    audio_file_path = play_sample(request)

    context = {
        "user_input": user_input,
        "audio_file_path": audio_file_path,
    }
    return render(request, "index.html", context)
