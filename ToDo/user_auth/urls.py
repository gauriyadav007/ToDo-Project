from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login_/', views.login_, name='login_'),
    path('logout_/', views.logout_, name='logout_'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile')
]
