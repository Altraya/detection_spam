from django.conf.urls import url, patterns
from . import views

urlpatterns =  patterns('clustering.views', 
	url(r'^accueil$', 'home'),
	url(r'^screen/(\d+)$', views.view_screen),
)
