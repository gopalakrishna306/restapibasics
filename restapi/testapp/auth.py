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





### updated 

class custauthencation(BaseAuthentication):
    def authenticate(self, request):
        # name=request.GET.get('name')
        tokenn = request.GET.get('token')
        # if name==None or tokenn==None:
        if  tokenn == None:
            raise AuthenticationFailed('please  valid token woth yur end point')
            # raise AuthenticationFailed('please send valid name and valid token')
        try:
            # nam=token.objects.get(name=name,tokenno=tokenn)
            tokens = token.objects.get(tokenno=tokenn)        # idf token in token model then it will check user in user model and return
            user = User.objects.get(username=tokens.name)     # and it return corrsponding user is user ntable not in token s table
            return (user,None)
        except :
            raise AuthenticationFailed ('please check your creditials are invalid')















