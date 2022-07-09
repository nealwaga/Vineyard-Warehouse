from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=40)
    product_image= CloudinaryField('image/', default="")
    description=models.CharField(max_length=40)
    product_price = models.PositiveIntegerField(null=False, blank=False, default=1)
    
    def __str__(self):
        return self.name


class Price(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE,null=True)
    firstupperrange = models.PositiveIntegerField(null=False, blank=False, default=1)
    firstlowerrange = models.PositiveIntegerField(null=False, blank=False, default=1)
    secondupperrange = models.PositiveIntegerField(null=False, blank=False, default=1)
    secondlowerrange = models.PositiveIntegerField(null=False, blank=False, default=1)
    thirdupperrange = models.PositiveIntegerField(null=False, blank=False, default=1)
    thirdlowerrange = models.PositiveIntegerField(null=False, blank=False, default=1)
    firstprice= models.PositiveIntegerField(null=False, blank=False, default=1)
    secondprice = models.PositiveIntegerField(null=False, blank=False,default=1)
    thirdprice = models.PositiveIntegerField(null=False, blank=False, default=1)


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)
    
    
class OrderItem(models.Model):
    order_id = models.ForeignKey('Orders', on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(null=True)


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= CloudinaryField('image/', default="")
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    
    @property
    def get_id(self):
        return self.user.id
    
    def __str__(self):
        return self.user.first_name


class Inventory(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    cost_per_item = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    quantity_in_stock = models.IntegerField(null=False, blank=False)
    quantity_sold = models.IntegerField(null=False, blank=False)
    sales = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    stock_date = models.DateField(auto_now_add=True)
    last_sales_date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name