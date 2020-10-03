from rest_framework.permissions import  SAFE_METHODS,BasePermission

class test(BasePermission):
    def has_permission(self, request, view):
        print('thisis data',request.user)
        print(request.user.__dict__)
        SAFE_METHODS=['POST','GET',"PUT","PATCH"]
        if    request.method in SAFE_METHODS:
            return True
        else:
            return False

        
        
#################
upated with some code in permissions  file



from rest_framework.permissions import  SAFE_METHODS,BasePermission

class test(BasePermission):
    def has_permission(self, request, view):
        print('thisis data',request.user)
        print(request.user.__dict__)
        # SAFE_METHODS=['POST',"GET","PUT","PATCH","DELETE"]
        SAFE_METHODS = ['POST', "GET","DELETE"]
        # if  request.user.is_staff==True and  request.method in SAFE_METHODS:     ## here iam checking wherterh person is admin or not and
        if  request.method in SAFE_METHODS:
            return True                                                          ## and his reqest method also
        else:
            return False

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
