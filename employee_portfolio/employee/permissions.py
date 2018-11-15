from rest_framework.permissions import BasePermission
from .models import Department


class IsEmployer(BasePermission):
    """Custom permission class to allow only employer of a department to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the employers of a particular department."""
        if isinstance(obj, Department):
            return obj.employer == request.user
        return obj.employer == request.user