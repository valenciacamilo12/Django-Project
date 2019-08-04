from django.conf.urls import url
from apps.clientes.views import ClienteCreate,ClienteUpdate,ClienteDelete,ClienteList

urlpatterns = [
    url(r'^nuevo$', ClienteCreate.as_view(), name = 'cliente_crear'),
    url(r'^listar$', ClienteList.as_view(), name = 'cliente_listar'),
    url(r'^editar/(?P<pk>[\d]+)/$', ClienteUpdate.as_view(), name = 'cliente_editar'),
    url(r'^eliminar/(?P<pk>[\d]+)/$', ClienteDelete.as_view(), name = 'cliente_eliminar'),
]