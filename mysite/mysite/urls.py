"""
URL configuration for mysite project.

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
from django.urls import path,include
# from app_1 import views as views_1
# from app_2 import views as views_2
from app_1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('app_1/', include('app_1.urls')),
    path('app_2/',include('app_2.urls')),

    path('',views.main)
   

    # path('admin/', admin.site.urls),
    # path('app_1/', views_1.app_1, name="app_1"),
    # path('app_2/', views_2.app_2, name="app_2"),
    # path('', views_1.index, name="index"),
]
