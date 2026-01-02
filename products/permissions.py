from rest_framework import permissions

from .models import Product

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        if request.method in ['PUT', 'PATCH', 'DELETE']:
            product_id = request.resolver_match.kwargs.get('pk')

            try:
                product = Product.objects.get(id=product_id)

                if product.user == request.user:
                    return True

                return False
            except Product.DoesNotExist:
                return True

        return True