from rest_framework.permissions import  BasePermission



class MyPermission(BasePermission):
   def has_permission(self, request, view):
        if  request.user.is_superuser:
            if  request.method == "GET" or  request.method == "POST" or request.method == "PUT" or  request.method == "DELETE"  :
                return True
        elif request.user.is_staff:
            if  request.method == "GET" or  request.method == "POST" or request.method == "PUT":
                return True
        elif request.user.is_active:
            if  request.method == "GET" or  request.method == "POST" :
                return True
        else:
            return False


