from django.conf.urls import url
from . import views

urlpatterns = [
    # /receitas/
    url(r'^$', views.index, name='index'),

    #receitas/712/
    url(r'^(?P<prescricao_id>[0-9]+)/$', views.detail, name='detail'),
]
