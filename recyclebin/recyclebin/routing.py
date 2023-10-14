from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from django.urls import re_path

from core import consumers


websocket_urlpatterns = [
    re_path(r'ws/image_updates/$', consumers.ImageUpdateConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})
