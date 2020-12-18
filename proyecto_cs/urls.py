"""proyecto_cs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from work_day import views
from work_day.forms import (
    UserPasswordResetForm,
    UserPasswordResetConfirmForm,
)

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', views.login, name='login'),
    path('logout/', views.logout),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('messages/', views.messages),
    path('user/editProfile/', views.edit_profile, name='edit_profile'),
    path('user/addJob/', views.add_job, name='add_job'),
    path('user/addStudy/', views.add_study, name='add_study'),
    path('user/editStudy/<int:pk>', views.add_study, name='edit_study'),
    path('user/editJob/<int:pk>', views.add_job, name='edit_job'),
    path('employments/', views.employments),
    path('professionals/', views.view_professionals),
    path('createOffer/', views.create_job_offer, name='create_offer'),
    path('editOffer/<int:pk>', views.create_job_offer, name='edit_offer'),
    path('user/user-profile/', views.user_profile, name='user_profile'),
    path('user/user-profile/<int:pk>', views.user_profile),
    path('pantallaprincipal/', views.pantallaprincipal),
    path('prueba/', views.prueba),
    path('nuevoprincipal/', views.nuevoprincipal),
    path('jobOffers/<int:offer_id>/', views.job_offer, name='job_offer'),
    path('jobOffers/', views.job_offer, name='job_offer'),
    path('my_posts/', views.my_posts),

    path('resetPassword/',
         auth_views.PasswordResetView.as_view(
             template_name='users/recover.html',
             form_class=UserPasswordResetForm,
         ),
         name='reset_password'),
    path('resetPasswordSent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/resetPasswordSent.html',
         ),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/reset.html',
             form_class=UserPasswordResetConfirmForm,
         ), name='password_reset_confirm'),
    path('resetPasswordComplete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/resetPasswordComplete.html',
         ), name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
