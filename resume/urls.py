from django.conf.urls import url

from . import views

app_name = 'resume'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^save_message/$', views.save_message, name='save_message'),
]
