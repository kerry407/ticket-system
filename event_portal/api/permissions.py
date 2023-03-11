from rest_framework import permissions 


class EventHostPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.event_hoster


class EventHostORReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True 
        return request.user == obj.host
    

class IsAdminOrReadOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True 
        return request.user.is_staff 