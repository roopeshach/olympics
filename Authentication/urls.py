from django.urls import path

from . import views
urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.logout_user, name='logout'),
    path('change-password/<int:id>', views.change_password, name='change-password'),
    path('reset-password', views.reset_password, name='reset-password'),
    path('verify-otp/<int:id>', views.verify_otp, name='verify-otp'),
    path('user-profile', views.user_profile, name='user-profile'),
  
]