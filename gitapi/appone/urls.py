from django.conf.urls import url

from appone import views

app_name = 'basic'

urlpatterns = [
    #url(r'^gitdata/$', views.home, name='home'),
    url(r'^more/$', views.more_info,name="more_info"),
    url(r'stack/$',views.stackoverflow,name="stackoverflow"),
]