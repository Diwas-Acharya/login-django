from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('userlogin/', views.login),
    path('userregister/', views.register)
]