from django.shortcuts import render
from rest_framework import generics
from .models import Tires, Category
from .serializers import(
    TiresCreateSerializer,
    CategorySerializer,
    TiresListSerializer,
)
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(
        tags=['category'],
        operation_description="Получить список всех категорий."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['category'],
        operation_description="Создать новую категорию."
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TiresCreateView(generics.CreateAPIView):
    queryset = Tires.objects.all()
    serializer_class = TiresCreateSerializer

    @swagger_auto_schema(
        tags=['product'],
        operation_description="Этот эндпоинт позволяет создать новый продукт."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TiresListView(generics.ListAPIView):
    queryset = Tires.objects.all()
    serializer_class = TiresListSerializer