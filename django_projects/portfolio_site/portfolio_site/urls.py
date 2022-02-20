from django.contrib import admin
from django.urls import path, include
#from quote_generator import views

#make sure to change the location of import views
from portfolio import views
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('exchange_rate_calculator/', include('exchange_rate_calculator.urls')),
    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
