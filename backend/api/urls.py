from django.urls import path, include
from Django_SolarPV_Proj.router import router


urlpatterns = [
    path('api/', include(router.urls))
]