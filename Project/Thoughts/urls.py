from django.urls import path
from . import views


urlpatterns = [
    path('', views.my_profile_redirect, name = 'my_profile_redirect'),
    path('<str:pk>/', views.profile, name='profile'),
    path('add_comment/<int:pk_user>/<int:pk_post>', views.add_comment, name='add_comment'),
    path('edit/', views.edit, name='edit'),
]