from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import ProductSerializer
# Create your views here.
from .models import Product


class ProductListView(ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class= ProductSerializer


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class= ProductSerializer