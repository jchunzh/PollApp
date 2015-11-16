from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^create$', views.create, name='create'),
    url(r'^vote$', views.vote, name='vote')
]