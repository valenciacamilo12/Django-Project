from django.conf.urls import url
from apps.oficinas.views import OficinaCreate,OficinaUpdate,OficinaDelete,OficinaList

urlpatterns = [
    url(r'^nuevo$', OficinaCreate.as_view(), name = 'oficina_crear'),
    url(r'^listar$', OficinaList.as_view(), name = 'oficina_listar'),
    url(r'^editar/(?P<pk>[\d]+)/$', OficinaUpdate.as_view(), name = 'oficina_editar'),
    url(r'eliminar/(?P<pk>[\d]+)/$', OficinaDelete.as_view(), name = 'oficina_eliminar'),
]