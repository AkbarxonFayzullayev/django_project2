
from django.contrib import admin
from django.urls import include

from app1.urls import *
# from app2.urls import *
from app3.urls import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('funksiyaa/',funcn1),
    path('app/',include('app1.urls')),
    path('app2/',include('app2.urls')),
    path('app3/',include('app3.urls')),
]
