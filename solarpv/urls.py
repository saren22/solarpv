from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('register.html', views.register, name="register"),
    path('dashboard.html', views.dashboard, name="dashboard"),
]
