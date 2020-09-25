from rest_framework import permissions


class WriteAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            if request.user.is_student and not request.user.is_professor:
                return False

        return True
