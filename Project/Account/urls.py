from . import views
from django.contrib.auth import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [ 
    path('login/', views.LoginView.as_view(redirect_authenticated_user = True), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='/project/account/login/'), name='logout'),
]