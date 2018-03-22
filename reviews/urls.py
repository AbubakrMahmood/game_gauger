from django.conf.urls import url
from reviews import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^featured/$', views.featured, name='featured.html'),
    url(r'^addgame/$',views.addgame,name='addgame'),


]
