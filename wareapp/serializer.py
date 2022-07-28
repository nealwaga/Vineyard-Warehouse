from dataclasses import fields
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *


#Create here

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
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    customer = serializers.StringRelatedField()

    class Meta:
        model = Cart
        fields = '__all__'

class PostCartSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),many=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)

    class Meta:
        model = Cart
        fields = '__all__'
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('name', 'product_image','product_price', 'description')

class AddProductSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),many=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)

    class Meta:
        model = Product
        # fields = ('name', 'product_image','product_price', 'description')
        fields ='__all__'
        
class UpdateProductSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),many=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)

    class Meta:
        model = Product
        fields ='__all__'
        # fields = ('name', 'product_image', 'product_price', 'description')

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields ='__all__'
        # fields = ('user','product','email','address','mobile','order_date','status')
        

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('name','cost_per_item', 'quantity_in_stock', 'quantity_sold', 'sales', 'stock_date','last_sales_date')

class AddInventorySerializer(serializers.ModelSerializer):
    inventory = serializers.PrimaryKeyRelatedField(queryset=Inventory.objects.all(),many=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)

    class Meta:
        model = Inventory
        # fields = ('name', 'product_image','product_price', 'description')
        fields ='__all__'
        

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('order_id', 'quantity')

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('product_id', 'boxes', 'amount')
        
class DeleteProductSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),many=False)
    # user = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(),many=False)

    class Meta:
        model = Product
        fields ='__all__'



class EditProfileSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=False)

    class Meta:
        model = User
        fields ='__all__'
        fields = ('user','profile_pic', 'address','mobile')




# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields ='__all__'
#         # fields = ('user','profile_pic', 'address','mobile')

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)

#         token['username'] = user.username
#     return token