from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('change-info/', views.user_change, name='change_info'),

    path('change-password/', PasswordChangeView.as_view(template_name='users/change_password.html'),
         name='change_password'),
    path('change-password-done/', PasswordChangeDoneView.as_view(template_name='users/change_password_done.html'),
         name='password_change_done'),
]
