"""server_McMurphy URL Configuration

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
#서버 주소 결정 파일

from django.contrib import admin #관리자 페이지 쓸지?
from django.urls import path
from McMurphy.views import Main

#앱 내용을 html파일로 불러 오기 위한 
urlpatterns = [
        path('', Main.as_view()), 
        path('admin/', admin.site.urls) #관리자 페이지 쓸지?
]
