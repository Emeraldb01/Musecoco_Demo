from django.shortcuts import render

import uuid

from . import musecoco

def user_text_input(request):
    request_uuid = str(uuid.uuid4())
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '') 
        try:
            #executor.submit(musecoco, user_input)
            musecoco.generate(user_input)
            # print("dummy")
        except:
            user_input = "An error occured"
    else:
        user_input = ''

    print(f"{user_input=}")

    context = {'user_input': user_input, 'generation_finished': True}
    return render(request, 'download.html', context)
