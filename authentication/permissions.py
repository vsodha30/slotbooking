from rest_framework import permissions


class IsEmployeeOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, employee):
        if request.user:
            return employee == request.user
        return False