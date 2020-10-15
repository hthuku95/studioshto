from . import views
from django.urls import path , include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(r'',views.services_view),
    path(r'animation/',views.animation_view),
    path(r'appview/',views.app_view),
    path(r'artview/',views.art_view),
    path(r'threed/',views.threed_view),
    path(r'webview/',views.web_view),
    path(r'gameview/',views.game_view),
]
