from django.urls import path
from . import views


urlpatterns = [
    path('add_comment/<int:pk_user>/<int:pk_post>', views.add_comment, name='add_comment'),
    
    path('edit/', views.edit, name='edit'),
    path('edit/info', views.edit_info, name='edit_info'),
    path('edit/pass', views.edit_pass, name='edit_pass'),

    path('', views.my_profile_redirect, name = 'my_profile_redirect'),
    path('<str:pk>/', views.profile, name='profile'),

    path('addthought/,', views.addthought, name='addthought'),
]