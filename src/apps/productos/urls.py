from apps.productos.views import ProductoCreate,ProductoUpdate,ProductoDelete,ProductoList,GamaProductoCreate,GamaProductoUpdate,GamaProductoDelete,GamaProductoList
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^nuevo$', login_required(ProductoCreate.as_view()), name = 'producto_crear'),
    url(r'^gama/nuevo$', login_required(GamaProductoCreate.as_view()), name = 'productogama_crear'),
    url(r'^listar$', ProductoList.as_view(), name = 'producto_listar'),
    url(r'^gama/listar$', login_required(GamaProductoList.as_view()), name = 'productogama_listar'),
    url(r'^editar/(?P<pk>[\d]+)/$', login_required(ProductoUpdate.as_view()), name = 'producto_editar'),
    url(r'^eliminar/(?P<pk>[\d]+)/$', login_required(ProductoDelete.as_view()), name = 'producto_eliminar'),
    url(r'^gama/editar/(?P<pk>[\d]+)/$', login_required(GamaProductoUpdate.as_view()), name = 'productogama_editar'),
    url(r'^gama/eliminar/(?P<pk>[\d]+)/$', login_required(GamaProductoDelete.as_view()), name = 'productogama_eliminar'),

]