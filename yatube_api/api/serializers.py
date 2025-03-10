"""Модуль с определением сериализаторов проекта."""

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """Класс, определяющий сериализатор для постов."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        """Класс с метаданными модели поста."""

        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Класс, определяющий сериализатор для комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        """Класс с метаданными модели поста."""

        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    """Класс, определяющий сериализатор для групп."""

    class Meta:
        """Класс с метаданными модели группы."""

        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    """Класс, определяющий сериализатор для подписок."""

    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        """Класс с метаданными модели подписок."""

        model = Follow
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message=('Ошибка. Подписка уже оформлена.'),

            )
        ]

    def validate_following(self, data):
        """Валидация несовпадения пользователя и его подписки."""
        if self.context['request'].user == data:
            raise serializers.ValidationError(
                'Ошибка. Нельзя оформить подписку на самого себя.'
            )
        return data
