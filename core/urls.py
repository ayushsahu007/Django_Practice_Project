from django.contrib import admin
from home.views import *
from django.urls import include, path  

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 


urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('success_page/', success_page, name='success_page'),
    path('admin/', admin.site.urls),
    path("vegie/", include("vegie.urls")),
    path("account/", include("account.urls")),
    path("api/", include("api.urls")),


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root = settings.MEDIA_ROOT)
        
urlpatterns += staticfiles_urlpatterns()      
    