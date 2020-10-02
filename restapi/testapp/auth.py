from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication
from  testapp.models import token

class custauthencation(BaseAuthentication):
    def authenticate(self, request):
        name=request.GET.get('name')
        key = request.GET.get('key')              ### we hav to pass name as part of ery string
        print(name,key)
        nam=token.objects.get(name=name)
        if  key==nam.tokenno:
            return (nam,None)
        else:
            raise Exception

# class custauthencation(BaseAuthentication):
#     def authenticate(self, request):
#         name=request.POST.get('name')
#         age = request.POST.get('age')
#         print(name,age)                             ### we hav to pass name as part of bady
#         if name!= 'gk':
#             raise AuthenticationFailed
#         else:
#             return (name,None)