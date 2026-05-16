from django.urls import path
from . import views
from accounts import views as account_views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contractors/', views.contractor_list, name='contractor_list'),
    path('contractors/<int:pk>/', views.contractor_detail, name='contractor_detail'),
    path('jobs/<int:job_pk>/inquire/', views.send_inquiry, name='send_inquiry'),
    path('accounts/register/contractor/', account_views.register_contractor, name='register_contractor'),
    path('accounts/register/homeowner/', account_views.register_homeowner, name='register_homeowner'),
]