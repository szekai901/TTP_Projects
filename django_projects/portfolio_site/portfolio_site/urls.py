from django.contrib import admin
from django.urls import path, include
#from quote_generator import views

from portfolio import views
from blog import views
from django.conf.urls.static import static
from django.conf import settings 

def home(request):
    return render(request, "blog/home.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index, name='index'),
    path('', views.home, name='home'),
    #path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
