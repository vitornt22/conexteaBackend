from rest_framework.permissions import BasePermission

class IsSuperUserOrSchoolUser(BasePermission):
    """
    Permite apenas superusuário ou usuário vinculado a uma escola.
    """

    def has_permission(self, request, view):
        user = request.user
        # Permite se for superusuário
        if user.is_superuser:
            return True

        # Aqui você ajusta conforme sua lógica: exemplo:
        # Permite se o user tiver uma relação com School (você precisa ter isso no seu modelo de user)
        # Exemplo: se você estendeu o User e tem um campo school
        if hasattr(user, 'school') and user.school is not None:
            return True

        return False
