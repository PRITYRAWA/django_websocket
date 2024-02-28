from django.shortcuts import render


def chat_box(request, chat_box_name):
    # Your view logic here
    return render(request, 'chatbox.html', {'chatbox_name': chat_box_name})