from django.urls import path
from . import views

urlpatterns = [
    path('', views.friends, name='friends'),
    path('accept/<str:pk>/<str:page>/', views.accept, name='accept'),
    path('follow/<str:pk>/', views.follow, name='follow'),
    path('unfollow/<str:pk>/<str:page>/', views.unfollow, name='unfollow'),
    path('unfriend/<str:pk>/<str:page>/', views.unfriend, name='unfriend'),
]