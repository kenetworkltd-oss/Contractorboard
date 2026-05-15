from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/contractor/', views.register_contractor, name='register_contractor'),
    path('register/homeowner/', views.register_homeowner, name='register_homeowner'),
]