from django.conf.urls import patterns, url
from ships_main import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
	url(r'^ships/rnavy/', views.rnavy_index, name='rnavy_index'),
)
