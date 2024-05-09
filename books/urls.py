from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from backoffice.views import *
from books import settings

urlpatterns = [
    path('', index, name='index'),    
    path('admin/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
