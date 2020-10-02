"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework import routers
# import  testapp
router = routers.DefaultRouter()
from  testapp import views
router.register(r'api', views.StudentViewSet)
from rest_framework.authtoken import views as views2
from rest_framework.authtoken.views import  ObtainAuthToken
## jwt implatemation
from rest_framework_simplejwt.views import  token_obtain_pair,token_refresh,token_verify



urlpatterns = [
    path('admin/', admin.site.urls),
    path('testapp/',include('testapp.urls')),
    path('', include(router.urls)),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('gettoken/', views2.obtain_auth_token),
    path('getjwttoken/',token_obtain_pair),
    path('refreshjwttoken/',token_refresh),
    path('verfyjwttoken/',token_verify)





]
