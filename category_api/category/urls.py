from django.conf.urls import include, re_path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    re_path('^', include(router.urls)),
]