from django.urls import path
from .views import *

urlpatterns = [
    path('list/favorite/',FavoriteListApiView.as_view(),name='list_favorites'),
    path('create/favorite/',FavoriteCreateApiView.as_view(),name='create_favorites'),
    path('detail/favorite/<int:pk>/',FavoriteDetailApiView.as_view(),name='detail_favorites'),
    path('delete/favorite/<int:pk>/',FavoriteDeleteApiView.as_view(),name='delete_favorites'),

    path("detail/user/favorite/<int:pk>/", UserDetailFavoriteView.as_view(), name="detail_user"),

]