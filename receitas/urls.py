from django.conf.urls import url
from . import views

app_name = 'receitas'

urlpatterns = [
    # /receitas/
    url(r'^$', views.index, name='index'),

    # /receitas/<album_id>/
    url(r'^(?P<prescricao_id>[0-9]+)/$', views.detail, name='detail'),

    # /receitas/<album_id>/favorite/
    #url(r'^(?P<prescricao_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
