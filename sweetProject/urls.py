from django.contrib import admin
from django.urls import path, include
import darkChoco.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', darkChoco.views.index, name='index'),
    path('darkChoco/', include('darkChoco.urls')),
    path('whiteChoco/', include('whiteChoco.urls')),
]
