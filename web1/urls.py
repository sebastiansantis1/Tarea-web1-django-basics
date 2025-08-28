from django.contrib import admin
from django.urls import path
from core import views 

urlpatterns = [
    path('historia/',views.historia,name="historia"),
    path('informacion/',views.informacion,name="informacion"),
    path('',views.home,name="home"),
    path('gallery/',views.gallery,name="gallery"),
    path('admin/', admin.site.urls),
]
