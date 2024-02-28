# from app import consumers
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# # URLs that handle the WebSocket connection are placed here.
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from web_channels import consumers

# from . import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/some_path/$', consumers.MyConsumer.as_asgi()),
# ]


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                path("ws/", consumers.MyConsumer.as_asgi()),
            ]
        )
    ),
})