from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('register/', views.register, name='register'),  # Registration
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin-only/', views.admin_only_view, name='admin_only'),


   # path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),  # Logout
]

  
  
  
  
   # path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

