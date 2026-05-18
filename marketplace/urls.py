

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contractors/', views.contractor_list, name='contractor_list'),
    path('contractors/<int:pk>/', views.contractor_detail, name='contractor_detail'),
    path('jobs/<int:job_pk>/inquire/', views.send_inquiry, name='send_inquiry'),
    path('faq/', views.faq, name='faq'),
    path('inquiries/<int:pk>/', views.inquiry_detail, name='inquiry_detail'),
]