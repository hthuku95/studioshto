from django.contrib import admin
from django.urls import path , include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',views.index_view),
    path(r'about/',views.about_view),
    path(r'services/',include('services.urls')),
    path(r'articles/',include('articles.urls')),
]
#appending the static files urls to the above media
urlpatterns += staticfiles_urlpatterns()
#how to upload media..appending the media url to the patterns above
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)