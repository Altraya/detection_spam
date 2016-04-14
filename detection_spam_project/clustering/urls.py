from django.conf.urls import url
from django.conf.urls import patterns
from . import views

urlpatterns =  patterns('clustering.views', 
	url(r'^accueil$', 'home'),
	url(r'^screen/(\d+)$', views.view_screen),
)
