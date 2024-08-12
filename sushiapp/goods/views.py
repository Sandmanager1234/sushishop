from django.db.models import Count
from rest_framework import generics

from .serializers import CategoryListSerializer, GoodSerializer
from .models import Good, Category


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response_data = {
            'status': 'success',
            'result': response.data
        }
        response.data = response_data
        return response


class GoodListAPIView(generics.ListAPIView):
    serializer_class = GoodSerializer
    queryset = Good.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)
        total = queryset.count()
        response_data = {
            'status': 'success',
            'result': response.data
        }
        response_data['total'] = total
        response.data = response_data
        return response
    

class GoodDetailAPIView(generics.RetrieveAPIView):
    serializer_class = GoodSerializer
    queryset = Good.objects.all()
    lookup_field = 'id'
