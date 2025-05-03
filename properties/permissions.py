from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Autorise tout le monde à lire,
    mais seul un admin peut écrire (POST, PUT, DELETE).
    """

    def has_permission(self, request, view):
        # Méthodes "lecture seule" autorisées pour tous
        if request.method in permissions.SAFE_METHODS:
            return True
        # Pour créer/modifier/supprimer : il faut être admin
        return request.user.is_authenticated and request.user.is_admin
