from django.shortcuts import render

def print_input(request):
    user_input = ""
    
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        print(f"User typed: {user_input}")

    return user_input

def play_sample(request):
    # Assuming 'sample.mp3' is in the 'static/music/' folder
    audio_file_path = 'static/music/abc.mp3'
    return audio_file_path

def index(request):
    user_input = print_input(request)
    audio_file_path = play_sample(request)

    context = {'user_input': user_input, 'audio_file_path': audio_file_path}
    return render(request, 'index.html', context)
