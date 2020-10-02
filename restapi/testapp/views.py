from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from testapp.models import  student
from django.http import JsonResponse
from testapp.forms import studentform
from rest_framework.views import APIView
from django.core.serializers import serialize
import json

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import  SAFE_METHODS,BasePermission
from testapp.serializers import studentSerializer
from testapp.permissions import test
from testapp.auth import custauthencation


def home(request):
    return HttpResponse( '<h1> this is home page</h1>')

def data(request):
    permission_list = student.objects.all().order_by('-id')
    permission_serialize = json.loads(serialize('json', permission_list))
    return JsonResponse({'data': permission_serialize})

def formrender(request):
    form=studentform()
    return render(request,'test.html',{"form":form})

def save(request):
    form = studentform()
    name=request.POST.get('name')
    age = request.POST.get('age')
    sex = request.POST.get('sex')
    address = request.POST.get('address')
    student.objects.create(name=name,age=age,sex=sex,address=address)
    return render(request,'test.html',{"form":form})


from rest_framework.authentication import  TokenAuthentication
class StudentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    authentication_classes = [custauthencation]     # TokenAuthentication  # JWT authentacation
    permission_classes = [test]       #isADmin,ISAuthenticated,djangopermissionorReadyonlu



from rest_framework.response import Response

class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    def put(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    def delete(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    def patch(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

from testapp.models import token

def test(request):
    name=request.GET.get('name')   ##name=request.POST.get when dataposting as part of body   #get as part of qery string
    age=request.GET.get('age')
    print(name,age)
    return HttpResponse('workimg')

from django.contrib.auth.models import User

def tokengeneration(request):
    name= request.GET.get('name')
    print(name)
    user=User.objects.get(username=name)
    print(user.username)
    if user.username==name:
        s=token(name=name,tokenno=name+'test')
        if s.tokenno!=None:
            return HttpResponse('token alredy generste')
        else:
            s.save()

    else:
        raise Exception
    return HttpResponse('properly working')






















