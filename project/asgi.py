"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter,URLRouter

import userprofile.routing

from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application =ProtocolTypeRouter({

    'http': get_asgi_application(),
    'websocket':AuthMiddlewareStack(
       
       URLRouter(
        userprofile.routing.websocket_urlpatterns
       )

    )
})

# import os

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator
# from django.core.asgi import get_asgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# # Initialize Django ASGI application early to ensure the AppRegistry
# # is populated before importing code that may import ORM models.
# django_asgi_app = get_asgi_application()

# import userprofile.routing

# application = ProtocolTypeRouter({
#   "http": django_asgi_app,
#   "websocket": AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 userprofile.routing.websocket_urlpatterns
#             )
#         )
#     ),
# })
