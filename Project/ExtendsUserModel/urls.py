from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.show_users, name='show_users'),
    path('<int:pk>/profile/', views.profile, name='profile'),
]