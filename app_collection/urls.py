from django.urls import path
from app_collection.views import (RecommendationListApiView, RecommendationCreateApiView, RecommendationRUDApiView, 
NewCollectionRUDApiView, NewCollectionCreateApiView, NewCollectionListApiView)


urlpatterns = [
    path('list/collection/', NewCollectionListApiView.as_view()),
    path('create/collection/', NewCollectionCreateApiView.as_view()),
    path('rud/collection/<int:id>/', NewCollectionRUDApiView.as_view()),


    path('list/recommendation/', RecommendationListApiView.as_view()),
    path('create/recommendation/', RecommendationCreateApiView.as_view()),
    path('rud/recommendation/<int:id>/', RecommendationRUDApiView.as_view()),
]