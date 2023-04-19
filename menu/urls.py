"""menu URL Configuration

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
from django.urls import path
from mainapp.views import MainPageView

urlpatterns = [
    path('admin/', admin.site.urls),
path('', MainPageView.as_view(), name="main_page"),
path('private/', MainPageView.as_view(), name="main_page"),
path('sign_in/', MainPageView.as_view(), name="main_page"),
path('reset_password/', MainPageView.as_view(), name="main_page"),
path('sign_up/', MainPageView.as_view(), name="main_page"),
path('articles/', MainPageView.as_view(), name="main_page"),
path('creative/', MainPageView.as_view(), name="main_page"),
path('real/', MainPageView.as_view(), name="main_page"),
path('questions/', MainPageView.as_view(), name="main_page"),
path('suppose/', MainPageView.as_view(), name="main_page"),
]
