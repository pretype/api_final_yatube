"""Модуль с вьюсетами приложения api проекта Api_yatube."""

from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    """Класс с определением представления поста."""

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Записывает в БД текущего пользователя автором поста."""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Класс с определением представления комментариев."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly)

    def get_post_or_404(self):
        """Отдаёт определенный пост или ошибку 404."""
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        """Переопределяет метод, для фильтрования комментариев."""
        return self.get_post_or_404().comments.all()

    def perform_create(self, serializer):
        """Записывает в БД пост и текущего пользователя автором комментария."""
        serializer.save(author=self.request.user, post=self.get_post_or_404())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Класс с определением представления группы."""

    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class FollowViewSet(viewsets.ViewSetMixin, ListCreateAPIView):
    """Класс с определением представления подписок."""

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Отдаёт список подписок."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """Сохраняет подписку."""
        serializer.save(user=self.request.user)
