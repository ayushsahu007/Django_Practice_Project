from django.contrib import admin
from django.urls import path
from home.views import *
from vegie.views import *
from account.views import register, login_page, logout_page
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns   


urlpatterns = [
    path('', home, name='home'),
    path('receipes/', receipes, name = 'receipes'),
    path('delete-receipes/<int:id>/', delete_receipe, name='delete_receipes'),  
    path('update-receipe/<int:id>/', update_receipe, name='update_receipe'),    
  
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('success_page/', success_page, name='success_page'),
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', login_page, name='login'),
    path("logout/", logout_page, name="logout"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root = settings.MEDIA_ROOT)
        
urlpatterns += staticfiles_urlpatterns()      
    