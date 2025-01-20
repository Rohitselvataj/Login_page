from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('admin/create-post/', views.admin, name='admin'),
    path('user/posts/', views.user, name='user'),
]
