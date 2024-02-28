from django.urls import path

from .views import chat_box

urlpatterns = [
    path('chat/<str:chat_box_name>/', chat_box, name='chat_box'),
    # Other URL patterns as needed
]
