from django.conf.urls import url 
from januszex import views
 
urlpatterns = [ 
    url(r'^api/warehouse/global$', views.globalWarehouseList),
    url(r'^api/warehouse/global/(?P<pk>[0-9]+)$', views.globalWarehouseDetail),
    url(r'^api/warehouse/global/filter/(?P<pole>[A-Za-z0-9]+)=(?P<value>[A-Za-z0-9]+)$', views.globalWarehouseFilter),
    url(r'^api/warehouse/local$', views.localWarehouseList),
    url(r'^api/warehouse/local/(?P<pk>[0-9]+)$', views.localWarehouseDetail),
    url(r'^api/warehouse/local/filter/(?P<pole>[A-Za-z0-9]+)=(?P<value>[A-Za-z0-9]+)$', views.localWarehouseFilter),
    url(r'^api/postal-code$', views.rangePostalCodeList),
    url(r'^api/postal-code/(?P<pk>[0-9]{2}-[0-9]{3})$', views.rangePostalCodeDetail),
    url(r'^api/warehouse/local/(?P<value>[0-9]+)/postal-code$', views.rangePostalCodeFromWarehouse),#dodany 
    url(r'^api/getWarehouseFromCode$', views.getLocalWarehouseFromPostalCode),# wyrzucic 
    url(r'^api/parcel-track$', views.getTrack)
]