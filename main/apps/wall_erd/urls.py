from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^messages$', views.create_message),
	url(r'^messages/(?P<id>\d+)$', views.create_comment)
]