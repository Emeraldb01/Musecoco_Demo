from django.shortcuts import render
from django.http import HttpResponse

import mimetypes
import os
import concurrent.futures

executor = concurrent.futures.ThreadPoolExecutor(1)


def print_input(request):
    user_input = ""

    if request.method == "POST":
        user_input = request.POST.get("user_input", "")
        print(f"User typed: {user_input}")

    return user_input


def index(request):
    context = {"user_input": "", "generation_finished": False}
    return render(request, "index.html", context)


def download_midi(request):
    file_path = "/home/alpaca/musecoco_test/muzic/musecoco/2-attribute2music_model/generation/0505/linear_mask-1billion-attribute2music/infer_pipeline/topk15-t1.0-ngram0/0/midi/1.mid"

    with open(file_path, "rb") as file:
        response = HttpResponse(
            file.read(), content_type=mimetypes.guess_type(file_path)[0]
        )
        response[
            "Content-Disposition"
        ] = f'attachment; filename="{os.path.basename(file_path)}"'
        return response
