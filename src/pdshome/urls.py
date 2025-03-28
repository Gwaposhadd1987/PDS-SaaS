"""
URL configuration for pdshome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from auth import views as auth_views
from .views import test_home_view, old_home_view, home_view, about_view

urlpatterns = [
    
    path('', old_home_view), # index page --> root page
    path('home/', home_view),
    path('login/', auth_views.login_view),
    path('register/', auth_views.register_view),
    path('about/', about_view),
    path('test-home/', test_home_view), # the home_page_view function is used as a callback handler
    path('admin/', admin.site.urls),
]
