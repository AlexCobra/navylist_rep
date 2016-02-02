from django.conf.urls import patterns, url
from ships_main import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
	url(r'^ships/rnavy/', views.rnavy_index, name='rnavy_index'),
        url(r'^ships/rnavy/', views.ShipCreate.as_view(), name='ship-add'),
        url(r'^ships/rnavy/(?P<pk>[0-9]+)/$', views.ShipUpdate.as_view(), name='ship-update'),
        url(r'^ships/rnavy/(?P<pk>[0-9]+)/delete/$', views.ShipDelete.as_view(), name='ship-delete'),
)
