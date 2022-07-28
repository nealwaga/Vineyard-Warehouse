from ast import Is
from re import I
from uuid import RESERVED_FUTURE
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, generics
import json

from .models import *
from .serializer import *


# Create your views here.
# class RegisterView(generics.CreateAPIView):

#     def post(self, request):
#         # queryset = User.objects.all()
#         # permission_classes = (AllowAny,)
#         # serializer_class = RegisterSerializer

#         print("Hello")

#         data = json.loads(request.body)
#         # print (data)
        
#         print (data['username'])
#         print (data['password'])
#         print (data['email'])

#         new_data = User.objects.create_user(username=data['username'],
#                                             password=data['password'],
#                                             email=data['email'])

#         # new_data.save()
#         return Response("User created successfully!")

# class CustomerList(APIView):
#     permission_classes = (AllowAny, )
    
#     def get(self, request, format=None):
#         all_customer = Customer.objects.all()
#         serializers = CustomerSerializer(all_customer, many=True)
#         return Response(serializers.data)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
        
    
class ProductList(APIView):
    # permission_classes = (IsAuthenticated, AllowAny )
    
    def get(self, request):
        if request.method == 'GET':
            all_product = Product.objects.all()
            serializers = ProductSerializer(all_product, many=True)
            return Response(serializers.data)

    def delete(self,request):
        if request.method == 'DELETE':

            if 'product' in request.GET and request.GET['product']:
                product = request.GET['cart']
                product = Cart.objects.filter(id=product)
                print(product)
                product.delete()

        return Response({"message":'item was deleted'})
    
    # def post(self):
    #     pass


class add_product(APIView):
    # permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request):
        # product = Product.objects.all()
        serializer = AddProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class update_product(APIView):
    # permission_classes = (IsAuthenticated, AllowAny)

    def put(self, request):
        serializer = UpdateProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class OrdersList(APIView):
    # permission_classes = (IsAuthenticated, AllowAny)
    
    def get(self, request):
        if request.method == 'GET':
            all_orders = Orders.objects.all()
            serializers = OrdersSerializer(all_orders, many=True)
            return Response(serializers.data)

    
class InventoryList(APIView):
    # permission_classes = (IsAuthenticated, AllowAny)
    
    def get(self, request):
        if request.method == 'GET':
            all_inventory= Inventory.objects.all()
            serializers = InventorySerializer(all_inventory, many=True)
            return Response(serializers.data)

    def delete(self,request):
        if request.method == 'DELETE':

            if 'inventory' in request.GET and request.GET['inventory']:
                inventory = request.GET['cart']
                inventory = Inventory.objects.filter(id=inventory)
                print(inventory)
                inventory.delete()

        return Response({"message":'item was deleted'})
        
    def post(self):
        pass
    
class add_inventory(APIView):
    # permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request):
        # inventory = Inventory.objects.all()
        serializer = AddInventorySerializer(data=request.POST)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderItemList(APIView):
    # permission_classes = (IsAuthenticated, AllowAny)
    
    def get(self, request):
        if request.method == 'GET':
            all_order_item = OrderItem.objects.all()
            serializers = OrderItemSerializer(all_order_item, many=True)
            return Response(serializers.data)
    

class PriceList(APIView):
    # permission_classes = (IsAuthenticated, AllowAny)
    
    def get(self, request):
        if request.method == 'GET':
            all_prices = Price.objects.all()
            serializers = OrderItemSerializer(all_prices, many=True)
            return Response(serializers.data)


class CartView (APIView):
    # permission_classes = (IsAuthenticated, AllowAny)

    def get(self, request):
        if request.method == 'GET':
            if 'user' in request.GET and request.GET['user']:
                user = request.GET['user']
                cart = Cart.objects.all()
            else:
                cart = Cart.objects.all()

            serializer = CartSerializer (cart, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = PostCartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self,request):
        if request.method == 'DELETE':

            if 'cart' in request.GET and request.GET['cart']:
                cart = request.GET['cart']
                cart = Cart.objects.filter(id=cart)
                print(cart)
                cart.delete()

        return Response({"message":'item was deleted'})


class EmptyCart(APIView):
    # permission_classes = (IsAuthenticated, AllowAny)

    def delete(Self,request):
        if request.method == 'DELETE':
            Cart.objects.all().delete()
        return Response({"message":'item was deleted '})


class all_users(APIView):

    def get(self, request):
        users = User.objects.all()
        if 'username' in request.GET and request.GET['username']:
            username = request.GET['username']
            users = User.objects.filter(username=username)
        else:
            users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)



class edit_profile(APIView):
    # permission_classes = (IsAuthenticated, AllowAny)

    def post(self, request):
        serializer = EditProfileSerializer(data=request.POST)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)



# class DeleteProductList(APIView):
#     # permission_classes = (IsAuthenticated, )

#     def delete(self, request):
#         serializer = DeleteProductSerializer(data=request.DELETE)

#         if serializer.is_valid():
#             serializer.delete()

#         return Response(serializer.data)