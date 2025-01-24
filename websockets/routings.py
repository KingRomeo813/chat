from django.urls import path
from .sockets import SocketConsumer
from .gemenia import GeminiConsumer

websocket_urlpatterns = [

    path('ws/socket/', SocketConsumer.as_asgi()),
    path('ws/geminai/', GeminiConsumer.as_asgi()),

]