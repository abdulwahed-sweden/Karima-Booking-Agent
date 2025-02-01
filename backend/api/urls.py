from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MatchingViewSet

router = DefaultRouter()
router.register(r'matching', MatchingViewSet, basename='matching')

urlpatterns = [
    path('', include(router.urls)),
]
