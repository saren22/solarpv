from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('register.html', views.register, name="register"),       #can be removed
    path('dashboard.html', views.dashboard, name="dashboard"),      ##can be removed
    path('certification-search', views.certificationSearch, name="certificationSearch"),
]
