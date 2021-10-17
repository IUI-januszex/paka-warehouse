from django.conf.urls import url 
from tutorials import views 
 
urlpatterns = [ 
    url(r'^api/magazynGlobalny$', views.magazynGlobalny_list),
    url(r'^api/magazynGlobalny/(?P<pk>[0-9]+)$', views.magazynGlobalny_detail),
    url(r'^api/magazynLokalny$', views.magazynLokalny_list),
    url(r'^api/magazynLokalny/(?P<pk>[0-9]+)$', views.magazynLokalny_detail)
]