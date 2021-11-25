from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('corretor/', views.corretor_list, name="corretor_list"),
    path('corretor/<int:pk>/', views.corretor_detail, name="corretor_detail")
]
