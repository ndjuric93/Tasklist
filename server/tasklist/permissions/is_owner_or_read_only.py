from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        """
        Check if method is safe for permission, otherwise check if owner is the user.
        """
        safe_methods = permissions.SAFE_METHODS + ('PATCH', )
        if request.method in safe_methods:
            return True
        return obj.user == request.user
