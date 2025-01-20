from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin/update/', views.admin_update, name='admin_update'),
]
