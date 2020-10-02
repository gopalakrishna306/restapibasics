
from   testapp  import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from  testapp.views import test,tokengeneration


urlpatterns = [
path('', views.home,name='home'),
path('data/',views.data,name='data'),
path('form/',views.formrender,name='forms'),
path('save/',views.save,name='save'),
path('test/',test),
path('tokengenetaion/',tokengeneration)

]