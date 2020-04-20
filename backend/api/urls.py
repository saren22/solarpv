from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', views.ProductView)
router.register('Certificates', views.CertificateView)
router.register('Services', views.ServiceView)

urlpatterns = [
    path('api', include(router.urls))
]