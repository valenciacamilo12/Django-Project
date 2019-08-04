from apps.productos.views import ProductoCreate,ProductoUpdate,ProductoDelete,ProductoList,GamaProductoCreate,GamaProductoUpdate,GamaProductoDelete,GamaProductoList
from django.conf.urls import url

urlpatterns = [
    url(r'^nuevo$', ProductoCreate.as_view(), name = 'producto_crear'),
    url(r'^gama/nuevo$', GamaProductoCreate.as_view(), name = 'productogama_crear'),
    url(r'^listar$', ProductoList.as_view(), name = 'producto_listar'),
    url(r'^gama/listar$', GamaProductoList.as_view(), name = 'productogama_listar'),
    url(r'^editar/(?P<pk>[\d]+)/$', ProductoUpdate.as_view(), name = 'producto_editar'),
    url(r'^eliminar/(?P<pk>[\d]+)/$', ProductoDelete.as_view(), name = 'producto_eliminar'),
    url(r'^gama/editar/(?P<pk>[\d]+)/$', GamaProductoUpdate.as_view(), name = 'productogama_editar'),
    url(r'^gama/eliminar/(?P<pk>[\d]+)/$', GamaProductoDelete.as_view(), name = 'productogama_eliminar'),

]