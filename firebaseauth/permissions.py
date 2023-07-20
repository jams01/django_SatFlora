from rest_framework import permissions

class StaffPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        return request.user.is_staff
