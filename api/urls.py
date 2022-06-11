from django.urls import path 
from . import views


urlpatterns = [
     path('notes/', views.notes),
     path('notes/<str:pk>/', views.note),
]
