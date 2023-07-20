from rest_framework import permissions

class StaffPermission(permissions.BasePermission):
    """
    This class is a permission class to check if the user is a staff member.
    """

    def has_permission(self, request, view):
        """
            This method perform the checking the staff status on the logged user.

            Args:
                request: the request object
                view: the view been accessed
            Return: 
                is_staff: a boolean about their staff status. 
        """
        return request.user.is_staff
