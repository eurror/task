from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def chat_box(request, chat_box_name):
    return render(request, "chatbox.html", {"chat_box_name": chat_box_name})
