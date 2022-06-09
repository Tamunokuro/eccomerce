from cgitb import html
import imp
from pipes import Template
from re import (template)
from unicodedata import name
from django.urls import (path)
from django.contrib.auth import views as auth_views
from . import views
from .forms import (UserLoginForm, PwdResetForm, PwdResetConfirmForm)
from django.views.generic import TemplateView

app_name = "account"
urlpatterns = [
    path('register/', views.accountregister, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.account_activate, name='activate'),
    path('login/', auth_views.LoginView.as_view(template_name='account/registration/login.html',
         form_class=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
    # User dashborad
    path('dashboard/',
         views.dashboard, name='dashboard'),
    path('profile/edit-profile/', views.user_edit, name='edit-profile'),
    path('profile/delete-profile/', views.user_delete, name='delete-profile'),
    path('profile/delete-confirmed/', TemplateView.as_view(
        template_name='account/user/deleteConfirmed.html'), name='delete_confirmed'),
    # Password Reset
    path('password-reset/', auth_views.PasswordResetView.as_view(
         template_name='account/user/passwordResetForm.html',
         success_url='password_reset_email_confirm',
         email_template_name='account/user/password_reset_email.html',
         form_class=PwdResetForm),
         name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='account/user/password_reset_confirm.html',
                                                                                                success_url='/account/password_reset_complete/',
                                                                                                form_class=PwdResetConfirmForm), name='password_reset_confirm'),
    path('password-reset/password_reset_email_confirm/', TemplateView.as_view(
        template_name='account/user/reset_status.html'), name='password_reset_done'),
    path('password_reset_complete/', TemplateView.as_view(
        template_name='account/user/reset_status.html'), name='password_reset_complete')
]
