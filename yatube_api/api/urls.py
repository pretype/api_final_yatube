"""Модуль с маршрутизацией приложения api проекта Api_yatube."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/?comments/?',
                CommentViewSet, basename='comment')
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')

api_version_patterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt'))
]

urlpatterns = [
    path('v1/', include(api_version_patterns)),
]
