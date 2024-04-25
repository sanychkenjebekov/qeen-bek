from django.shortcuts import render
from rest_framework.viewsets import generics
from app_collection.models import NewCollection, Recommendations
from app_collection.serializers import (NewCollectionCreateSerializer, NewCollectionListSerializer,
RecommendationCreateSerializer, RecommendationListSerializer)

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class NewCollectionCreateApiView(generics.CreateAPIView):
    queryset = NewCollection.objects.all()
    serializer_class = NewCollectionCreateSerializer



class NewCollectionListApiView(generics.ListAPIView): #Было 4 SQL запроса стало 3
    queryset = NewCollection.objects.all().prefetch_related('product')
    serializer_class = NewCollectionListSerializer

    @method_decorator(cache_page(60))  
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class NewCollectionRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewCollection.objects.all()
    serializer_class = NewCollectionCreateSerializer
    lookup_field = "id"








class RecommendationListApiView(generics.ListAPIView):
    queryset = Recommendations.objects.all().prefetch_related('product')  #Было 4 SQL запроса стало 3
    serializer_class = RecommendationListSerializer

    @method_decorator(cache_page(60))  
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class RecommendationCreateApiView(generics.CreateAPIView):
    queryset = Recommendations.objects.all()
    serializer_class = RecommendationCreateSerializer



class RecommendationRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recommendations.objects.all()
    serializer_class = RecommendationCreateSerializer
    lookup_field = "id"