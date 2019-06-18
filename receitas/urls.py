from django.conf.urls import url
from . import views

app_name = 'receitas'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /music/album/add/
    url(r'prescricao/add/$', views.AlbumCreate.as_view(), name='album-add'),
]
