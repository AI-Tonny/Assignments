from rest_framework import permissions

class IsJournalistCanOnlyCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.groups.filter(name='Journalists').exists():
            # TODO: ask about this moment (allow to do anything or just create)
            # if request.method == 'POST':
            #     return True
            # return False
            return True

        if request.user.is_superuser:
            return True

        return False