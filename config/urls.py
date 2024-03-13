from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_g/', include("app_g.urls")),
    path('app1/', include("app1.urls")),
    path('users/', include("users.urls")),

] 
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)