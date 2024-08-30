"""Модуль с определением пользовательских доступов."""

from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Класс, определяющий авторские и пользовательские права."""

    def has_object_permission(self, request, view, user_content_obj):
        """Проверяет доступ текущего пользователя к функциям приложения."""
        return (
            request.method in permissions.SAFE_METHODS
        ) or (
            user_content_obj.author == request.user
        )


class IsAuthorOnly(permissions.IsAuthenticated):
    """Класс, определяющий авторские и пользовательские права."""

    def has_object_permission(self, request, view, user_content_obj):
        """Проверяет доступ текущего пользователя к функциям приложения."""
        return user_content_obj.author == request.user
