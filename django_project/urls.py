"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from users.forms import UserPasswordResetForm, UserPasswordResetNewForm

from users.views import (
    registration_view,
    logout_view,
    login_view,
    activate,
    password_reset_view,
    test,
)

from blog.views import (
    BlogView,
    profile_view,
    self_profile_view,
    frontend_view,
)

urlpatterns = [

    # frontend development
    path('1', test, name="frontend"),

    # admin backend
    path('admin/', admin.site.urls),

    # index blog
    path('', include('blog.urls', namespace='blog')),

    # blog detail page
    # path('<user_netid>/<post_id>')

    # register, login, logout
    path('register/', registration_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),

    # password reset
    path('accounts/password/reset/', password_reset_view, name='password_reset'),

    path('accounts/password/reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset/password_reset_done.html'),
     name='password_reset_done'),
 
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'users/password_reset/password_reset_new.html',
        form_class= UserPasswordResetNewForm), name='password_reset_confirm'),
        
    path('accounts/password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset/password_reset_complete.html'),
     name='password_reset_complete'),
    
    # path for email verification
    path('activate/<uidb64>/<token>', activate, name='activate'),  
    
    path('<str:pk>/', profile_view.as_view(), name='profile'),
]


if settings.DEBUG:
    
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)