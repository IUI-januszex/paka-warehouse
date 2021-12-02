from django.conf.urls import url 
from januszex import views
 
urlpatterns = [ 
    url(r'^api/GlobalWarehouse$', views.globalWarehouseList),
    url(r'^api/GlobalWarehouse/(?P<pk>[0-9]+)$', views.globalWarehouseDetail),
    url(r'^api/globalWarehouseFilter/(?P<pole>[A-Za-z0-9]+)=(?P<value>[A-Za-z0-9]+)$', views.globalWarehouseFilter),
    url(r'^api/LocalWarehouse$', views.localWarehouseList),
    url(r'^api/LocalWarehouse/(?P<pk>[0-9]+)$', views.localWarehouseDetail),
    url(r'^api/localWarehouseFilter/(?P<pole>[A-Za-z0-9]+)=(?P<value>[A-Za-z0-9]+)$', views.localWarehouseFilter),
    url(r'^api/RangePostalCode$', views.rangePostalCodeList),
    url(r'^api/RangePostalCode/(?P<pk>[0-9]{2}-[0-9]{3})$', views.rangePostalCodeDetail),
    url(r'^api/getWarehouseFromCode$', views.getLocalWarehouseFromPostalCode),
    url(r'^api/getTrack$', views.getTrack)
]