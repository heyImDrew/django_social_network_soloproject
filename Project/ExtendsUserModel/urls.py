from django.urls import path
from . import views

urlpatterns = [
    path('', views.friends, name='friends'),
    path('accept/<int:pk>/<str:page>/', views.accept, name='accept'),
    path('follow/<int:pk>/', views.follow, name='follow'),
    path('unfollow/<int:pk>/<str:page>/', views.unfollow, name='unfollow'),
    path('unfriend/<int:pk>/<str:page>/', views.unfriend, name='unfriend'),
]