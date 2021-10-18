from django.conf.urls import url 
from tutorials import views 
 
urlpatterns = [ 
    url(r'^api/GlobalWarehouse$', views.GlobalWarehouse_list),
    url(r'^api/GlobalWarehouse/(?P<pk>[0-9]+)$', views.GlobalWarehouse_detail),
    url(r'^api/LocalWarehouse$', views.LocalWarehouse_list),
    url(r'^api/LocalWarehouse/(?P<pk>[0-9]+)$', views.LocalWarehouse_detail)
]