
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from web_channels import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channel_example.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                path("ws/127.0.0.1:8000/", consumers.MyConsumer.as_asgi()),
                # Add more WebSocket paths as needed
            ]
        )
    ),
})

