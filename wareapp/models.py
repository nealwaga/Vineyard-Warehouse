from contextlib import AbstractAsyncContextManager
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator
from contextlib import nullcontext
from unicodedata import name

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=40)
    product_image= CloudinaryField('image/', default="")
    description=models.CharField(max_length=40)
    product_price = models.PositiveIntegerField(null=False, blank=False, default=1)
    
    def __str__(self):
        return self.name

    def create_product(self):
        """
        A method that creates a product
        """
        self.save()

    def delete_product(self):
        """
        A method that deletes a product
        """
        self.delete()    

    @classmethod
    def update_product(cls, id):
        """
        A method that updates a product
        """
        product = cls.objects.filter(id=id).update(id=id)
        return product       

    @classmethod
    def find_product(cls, product_id):
        """
        A method that finds a product using its id
        """         
        product = Product.objects.filter(id=product_id)
        return product


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
    STATUS = (
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)
    
    
class OrderItem(models.Model):
    order_id = models.ForeignKey('Orders', on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(null=True)


# class Customer(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     # first_name = models.CharField(max_length=255,null=True)
#     profile_pic= CloudinaryField('image/', default="")
#     address = models.CharField(max_length=40)
#     mobile = models.CharField(max_length=20,null=False)
    
#     def __str__(self) -> str:
#         return self.user.username

#     @classmethod
#     def update_customer(cls, id):
#         """
#         A method that updates a customer
#         """
#         customer = cls.objects.filter(id=id).update(id=id)
#         return customer    


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

    def create_inventory(self):
        """
        A method that creates an inventory
        """
        self.save()

    def delete_inventory(self):
        """
        A method that deletes an inventory
        """
        self.delete()    

    @classmethod
    def update_inventory(cls, id):
        """
        A method that updates an inventory
        """
        inventory = cls.objects.filter(id=id).update(id=id)
        return inventory      


class Cart(models.Model):
    products = models.ForeignKey(Product, related_name='cart_products', on_delete=models.CASCADE)
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    # @property
    # def get_images(self):
    #     return self.cart_products.all()


class Profile(models.Model):
    """
    model for a user profile
    """
    user = models.OneToOneField(User, related_name="users", on_delete=models.CASCADE, default="")
    # user = models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.user.username

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @classmethod
    def save_profile(cls, profile):
        cls.save(profile)

    @classmethod
    def update_profile(cls, user):
        cls.update(user=user)

    @classmethod
    def delete_profile(cls, profile):
        cls.delete(profile)








# class AbstractBaseModel(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True

# class Products(AbstractBaseModel):
#     name=models.CharField(max_length=40)
#     product_image= CloudinaryField('image/', default="")
#     description=models.CharField(max_length=40)
#     product_price = models.PositiveIntegerField(null=False, blank=False, default=1)

#     def __str__(self):
#         return self.name

# class Customer(AbstractBaseModel):
#     name = models.CharField(max_length=200)
#     phone_number = models.CharField(max_length=200)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name