from rest_framework.permissions import BasePermission

class IsAuthenticatedWithRole(BasePermission):
    """
    Custom permission to only allow access to authenticated users
    who have a role of 'publisher', 'author', or 'simple'.
    """
    # Define the allowed roles
    allowed_roles = ['Publisher', 'Author', 'Simple']

    def has_permission(self, request, view):
        # First, check if the user is authenticated
        user = request.user
        if not user or not user.is_authenticated:
            return False

        # Check if the user has a role attribute.
        # Adjust this if your role is stored differently.
        user_role = getattr(user, 'user_type', None)
        if user_role is None:
            return False

        # Allow access if the user's role is in the allowed roles
        return user_role in self.allowed_roles