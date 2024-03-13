from django.urls import path
from app1 import views
from app1.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path("celulares_nuevos/ver", views.celularNuevoListView.as_view(), name="nuevoLista"),
path("celulares_nuevos/borrar/<int:pk>", views.celularNuevoDelete.as_view(), name="nuevoBorrar"),
path("celulares_nuevos/crear", views.celularNuevoCreateView.as_view(), name="nuevoCrear"),
path("celulares_nuevos/detalle/<int:pk>", views.celularNuevoDetailView.as_view(), name="nuevoDetalle"),
path("celulares_nuevos/editar/<int:pk>", views.celularNuevoUpdate.as_view(), name="nuevoEditar"),

  ]
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
  