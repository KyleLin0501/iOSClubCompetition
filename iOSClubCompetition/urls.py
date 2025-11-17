"""
URL configuration for iOSClubCompetition project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path
# 1. 不再需要 import 'include'
# 2. 從 registration.views 引入 home 視圖
from competition import views as registration_views

from django.contrib import admin
from django.urls import path


urlpatterns = [
    # path('admin/', admin.site.urls), # 您註解掉了，OK
    path('', registration_views.home, name='home'),
    path('registration/', registration_views.registration, name='registration'),
    path('dashboard/', registration_views.dashboard, name='dashboard'),
]