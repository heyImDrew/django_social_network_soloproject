from django.urls import path
from . import views

urlpatterns = [
    path('', views.messages, name='messages'),
    path('<int:pk>/', views.dialog, name='dialog'),
]