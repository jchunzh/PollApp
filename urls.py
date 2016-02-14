from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/poll', views.PollViewSet)

urlpatterns = [
    url(r'^create$', views.create, name='create'),
    url(r'^vote/.+$', views.vote, name='vote'),
    url(r'^results/.+$', views.results, name='results'),
    url(r'^', include(router.urls))
]

for u in router.urls: 
	print(u)