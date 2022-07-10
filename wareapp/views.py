from re import I
from uuid import RESERVED_FUTURE
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, generics

from .models import *
from .serializer import *


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class CustomerList(APIView):
    permission_classes = (AllowAny, )
    
    def get(self, request, format=None):
        all_customer = Customer.objects.all()
        serializers = CustomerSerializer(all_customer, many=True)
        return Response(serializers.data)
    
class ProductList(APIView):
    # permission_classes = (IsAuthenticated, )
    
    def get(self, request, format=None):
        all_product = Product.objects.all()
        serializers = ProductSerializer(all_product, many=True)
        return Response(serializers.data)
    
    def post(self):
        pass
    
class OrdersList(APIView):
    # permission_classes = (IsAuthenticated, )
    
    def get(self, request, format=None):
        all_orders = Orders.objects.all()
        serializers = OrdersSerializer(all_orders, many=True)
        return Response(serializers.data)
    
class InventoryList(APIView):
    # permission_classes = (IsAuthenticated, )
    
    def get(self, request, format=None):
        all_inventory= Inventory.objects.all()
        serializers = InventorySerializer(all_inventory, many=True)
        return Response(serializers.data)
    
    def post(self):
        pass
    
class OrderItemList(APIView):
    # permission_classes = (IsAuthenticated, )
    
    def get(self, request, format=None):
        all_order_item = OrderItem.objects.all()
        serializers = OrderItemSerializer(all_order_item, many=True)
        return Response(serializers.data)
    
class PriceList(APIView):
    # permission_classes = (IsAuthenticated, )
    
    def get(self, request, format=None):
        all_prices = Price.objects.all()
        serializers = OrderItemSerializer(all_prices, many=True)
        return Response(serializers.data)

# class AddProductList(APIView):
#     # permission_classes = (IsAuthenticated, )

#     def post(self, request):
#         product = Product.objects.all()
#         serializer = AddProductSerializer(data=request.POST)

#         if serializer.is_valid():
#             serializer.save()

#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class DeleteProductList(APIView):
#     # permission_classes = (IsAuthenticated, )

#     def delete(self, request):
#         serializer = DeleteProductSerializer(data=request.DELETE)

#         if serializer.is_valid():
#             serializer.delete()

#         return Response(serializer.data)

# class UpdateProductList(APIView):
#     # permission_classes = (IsAuthenticated, )

#     def post(self, request):
#         serializer = UpdateProductSerializer(data=request.POST)

#         if serializer.is_valid():
#             serializer.save()

#         return Response(serializer.data)

# class UpdateProfileList(APIView):
#     # permission_classes = (IsAuthenticated, )

#     def post(self, request):
#         serializer = UpdateProfileSerializer(data=request.POST)

#         if serializer.is_valid():
#             serializer.save()

#         return Response(serializer.data)

# class AddInventoryList(APIView):
#     # permission_classes = (IsAuthenticated, )

#     def post(self, request):
#         # inventory = Inventory.objects.all()
#         serializer = AddInventorySerializer(data=request.POST)

#         if serializer.is_valid():
#             serializer.save()

#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class AddToCartList(APIView):
#     # permission_classes = (IsAuthenticated, )

#     def post(self, request, format=None):
#         all_product = Product.objects.all()
#         serializers = ProductSerializer(all_product, many=True)