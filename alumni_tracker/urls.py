"""alumni_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views as project_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("", project_views.home, name="home"),
    path('accounts/', include('accounts.urls')),
    path('pathways/', include('pathways.urls')),

    
    # Authentication

    # Enter email and get a token in your inbox
     path("password-reset/", 
        auth_views.PasswordResetView.as_view(template_name="accounts/password-reset.html"), 
        name="password_reset"
    ),
    # Notice page for password successful reset form submission
    path("password-reset/done/", 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password-reset-done.html"), 
        name="password_reset_done"
    ),
    
    # Endpoint for updating password
    path("password-reset-confirm/<uidb64>/<token>/", 
        auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password-reset-confirm.html"), 
        name="password_reset_confirm"
    ),
    # Notify user if password was successfully updated
     path("password-reset-complete/", 
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password-reset-complete.html"
        ), 
        name="password_reset_complete"
    ),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
] 

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )