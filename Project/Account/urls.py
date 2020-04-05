from . import views
from django.contrib.auth import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import login, registration

urlpatterns = [ 
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('logout/', views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
]