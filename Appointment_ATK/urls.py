from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as authviews
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def H(request):
    return render(request,'_base.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', H, name="home"),
    path('Reserve/',include('Reserve.urls')),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

admin.site.index_title = "Appointment ATK"
admin.site.site_header = "Appointment ATK"
admin.site.site_title = "Appointment ATK"

