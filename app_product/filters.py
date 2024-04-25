from rest_framework import filters

class PriceRangeFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')

        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)

        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        return queryset



class SearchFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        title = request.query_params.get('search')
        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset
