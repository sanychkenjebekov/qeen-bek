from rest_framework import permissions, generics, response, status


from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from .models import Favorite
from .serializers import FavoriteListSerializer,UserFavoriteSerializer
from .permissions import IsUserOrAdmin

from app_product.models import Product, IsFavorite
from app_user.models import CustomUser

class FavoriteListApiView(generics.ListAPIView):
    queryset = Favorite.objects.all().select_related('product').prefetch_related('user',)
    serializer_class = FavoriteListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                # Если пользователь - администратор, возвращаем все объекты Favorite
                return Favorite.objects.all()
            else:
                # Возвращаем объекты Favorite только для текущего пользователя
                return Favorite.objects.filter(user=user)
        return Favorite.objects.none()
    
    # @method_decorator(cache_page(100))  
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


    


class FavoriteCreateApiView(generics.CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteListSerializer
    permission_classes = [permissions.IsAuthenticated]

    

    def create(self, request, *args, **kwargs):
        product_id = self.request.data['product']
        try:
            product = Product.objects.get(pk=product_id)
            if Favorite.objects.filter(user=request.user, product=product).exists():
                return response.Response({"error":"Product is already in favorites"}, status=status.HTTP_400_BAD_REQUEST)
        except Favorite.DoesNotExist:
            return response.Response({"error":"Product does not exist"})

        
        
        favorite = Favorite.objects.create(user=request.user, product=product)
        is_favorite_instance = IsFavorite.objects.create(user=request.user,favorite=favorite)
        product.is_favorite.add(is_favorite_instance)

        product.save()
        
        serializer = self.get_serializer(favorite)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)





        

    


class FavoriteDetailApiView(generics.RetrieveAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteListSerializer
    permission_classes = [permissions.IsAuthenticated]

    # @method_decorator(cache_page(60))  
    def get_queryset(self):
        return Favorite.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.filter(id=self.kwargs[self.lookup_field]).first()
        if obj is None:
            raise Http404("Product does not exist")
        return obj

class FavoriteDeleteApiView(generics.DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteListSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_object(self):
        try:
            # Получаем объект избранного по переданному идентификатору
            obj = self.queryset.get(pk=self.kwargs['pk'])
            # Проверяем, принадлежит ли объект текущему пользователю
            if obj.user != self.request.user:
                raise Http404("Вы не можете удалить этот объект избранного.")
            return obj
        except Favorite.DoesNotExist:
            raise Http404("Объект избранного не существует.")


    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            # Удаление объекта из модели Favorite
            self.perform_destroy(instance)
            # Удаление связанных объектов из модели IsFavorite
            IsFavorite.objects.filter(favorite=instance).delete()
            return response.Response({"success": "Deleted!"}, status=status.HTTP_204_NO_CONTENT)
        except Http404 as e:
            return response.Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)


class FavoriteUpdateApiView(generics.UpdateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteListSerializer
    permission_classes = [permissions.AllowAny]


class UserDetailFavoriteView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserFavoriteSerializer
    permission_classes = [permissions.IsAdminUser]