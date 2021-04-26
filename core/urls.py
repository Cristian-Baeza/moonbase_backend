from django.urls import path
from .views import current_user, UserList, FavoriteViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view())
]

router = DefaultRouter()
router.register(r'favorites', FavoriteViewSet, basename='favorite')
urlpatterns += router.urls