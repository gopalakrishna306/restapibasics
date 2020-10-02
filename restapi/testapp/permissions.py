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

