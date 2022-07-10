from dataclasses import fields
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *


#Create here

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)

#         token['username'] = user.username
#     return token

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            # address=validated_data['address'],
            # contact=validated_data['contact']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields ='__all__'
        # fields = ('user','profile_pic', 'address','mobile')
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'product_image','product_price', 'description')
        
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('customer','product','email','address','mobile','order_date','status')
        
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('name','cost_per_item', 'quantity_in_stock', 'quantity_sold', 'sales', 'stock_date','last_sales_date')
        
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('order_id', 'quantity')
        
class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('product_id', 'boxes', 'amount')
    
# class AddProductSerializer(serializers.ModelSerializer):
#     product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),many=False)
#     # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)

#     class Meta:
#         model = Product
#         # fields = ('name', 'product_image','product_price', 'description')
#         fields ='__all__'
        
# class DeleteProductSerializer(serializers.ModelSerializer):
#     product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),many=False)
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)

#     class Meta:
#         model = Product
#         fields ='__all__'

# class UpdateProductSerializer(serializers.ModelSerializer):
#     product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),many=False)
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)

#     class Meta:
#         model = Product
#         fields ='__all__'
#         # fields = ('name', 'product_image', 'product_price', 'description')

# class UpdateProfileSerializer(serializers.ModelSerializer):
#     customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(),many=False)
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)

#     class Meta:
#         model = Customer
#         fields ='__all__'
#         # fields = ('name', 'product_image', 'product_price', 'description')

# class AddInventorySerializer(serializers.ModelSerializer):
#     inventory = serializers.PrimaryKeyRelatedField(queryset=Inventory.objects.all(),many=False)
#     # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)

#     class Meta:
#         model = Inventory
#         # fields = ('name', 'product_image','product_price', 'description')
#         fields ='__all__'