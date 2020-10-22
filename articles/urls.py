from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.article_list, name= 'article_lists'),#homepage route for the articles app
    path(r'<slug>/',views.article_details, name='article_detail'),
    path(r'comment/<slug>/',views.article_comment),
    path(r'reply/<slug>/',views.article_reply),
    path(r'category/<slug>/',views.article_category, name= 'article_category'),
]