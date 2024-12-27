from django.urls import path
from .views import ItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

urlpatterns = []
urlpatterns += router.urls