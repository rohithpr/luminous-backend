from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_owner', views.get_owner),
    url(r'^descSquare', views.desc_square),
    url(r'^takeSquare', views.take_square),
    url(r'^markHome', views.mark_home),
    url(r'^isMine', views.isMine),
]
