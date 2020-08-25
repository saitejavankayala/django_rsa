from django.conf.urls import url
from api import views
urlpatterns = [
    url(r'^api/register$', views.registration),
    url(r'^api/login$', views.login),
]