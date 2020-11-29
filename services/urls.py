from . import views
from django.urls import path , include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path(r'',views.services_view),
    path(r'service_list/<slug>/',views.service_list),
]
