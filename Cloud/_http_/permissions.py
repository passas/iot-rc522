from rest_framework import permissions
from .models import User

class IsAgent(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user is None or not user.is_authenticated:
            return False
        return user.role == 'Agent'
    
class IsSuper(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user is None or not user.is_authenticated:
            return False
        return user.role == 'Super'
    
class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user is None or not user.is_authenticated:
            return False
        return user.role == 'Client'
    
class IsSensor(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user is None or not user.is_authenticated:
            return False
        return user.role == 'Sensor'