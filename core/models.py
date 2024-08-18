import uuid
from django.contrib.auth.models import  AbstractUser
from django.db import models


# Create your models here.

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} object (id: {self.id})"
    

# class User(BaseModel, AbstractUser):
#     first_name = models.CharField(max_length=50, blank=False)
#     last_name = models.CharField(max_length=50, blank=False)
#     username = models.CharField(max_length=50, blank=False)
#     email = models.EmailField(unique=True, null=True)
#     bio = models.TextField(null=True)
#     birth_date = models.DateField(null=True, blank=True)

#     avatar = models.ImageField(null=True, default="avatar.svg")

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
    

#     def __str__(self):
#         return f"{self.username} {self.first_name} {self.last_name}"


class InventoryItem(BaseModel):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-updated_at', '-created_at']
    
    def __str__(self):
        return self.__class__.object.all()
    

class Category(BaseModel):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.__class__.object.all()
        
class Product(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, default="avatar.svg")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    #category = models.DecimalField(Category, on_delete=models.SET_NULL, blank=True)  # New field
    
    class Meta:
        ordering = ['-updated_at', '-created_at']
     
    def __str__(self):
        return self.__class__.object.all()
    
class Supplier(BaseModel):
    name = models.CharField(max_length=255)
    contact_info = models.TextField(blank=True)
    business_name = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.__class__.object.all() 
    
# class Procurement(BaseModel):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('approved', 'Approved'),
#         ('ordered', 'Ordered'),
#         ('received', 'Received'),
#         ('cancelled', 'Cancelled'),
#     ]
    
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     supplier = models.ForeignKey("Supplier", on_delete=models.CASCADE)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     date = models.DateField()
    
#     class Meta:
#         ordering = ['-updated_at', '-created_at']
    
    # def __str__(self):
    #     return self.__class__.object.all()
    
    
class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    #price = models.BigIntegerField(null=True, blank=True)
    #total_price =
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.__class__.object.all()

class Demand(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    forecast_quantity = models.PositiveIntegerField()
    actual_quantity = models.PositiveIntegerField()
    date = models.DateField()
    
    class Meta:
        ordering = ['-updated_at', '-created_at']
    
    def __str__(self):
        return self.__class__.object.all()

    
class Supply(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='supplies')
    
    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.__class__.object.all()  
    
# class Logistics(BaseModel):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     status = models.CharField(max_length=50)
#     tracking_number = models.CharField(max_length=255, null=True, blank=True)
#     estimated_delivery = models.DateField(null=True, blank=True)
    
#     class Meta:
#         ordering = ['-updated_at', '-created_at']
    
#     def __str__(self):
#         return self.__class__.object.all()
    
# class Analytics(BaseModel):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
#     data = models.JSONField() #Not added to form yet
#     report_name = models.CharField(max_length=100)
#     report_data = models.TextField()
    
#     class Meta:
#         ordering = ['-updated_at', '-created_at']
    
#     def __str__(self):
#         return self.__class__.object.all()
    
# class Notification(BaseModel):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
#     message = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     read = models.BooleanField(default=False) #Not Added
    
#     class Meta:
#         ordering = ['-updated_at', '-created_at']
    
#     def __str__(self):
#         return self.__class__.object.all()