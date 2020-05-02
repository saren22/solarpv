from django.urls import path, include
from backend.api.views import ProductView, CertificateView, ServiceView
from rest_framework import routers
from solarpv.views import CertificateViewSet

router = routers.DefaultRouter()
router.register('products', ProductView)
router.register('Certificates', CertificateView)
router.register('Services', ServiceView)

router.register('certi-search', CertificateViewSet, basename='certisearch') 