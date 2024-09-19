from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserProfileManager
from django.utils.translation import gettext_lazy as _


# UserProfile Model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), max_length=60, unique=True)
    username = models.CharField(max_length=60, default=None)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Use lowercase for `category`
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/products/', blank=True, null=True)
    
    def __str__(self):
        return self.name


# Inventory Model
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Corrected to link to Product
    quantity = models.PositiveIntegerField()
    reorder_level = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name  # Referring to the product name


# Supplier Model
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name


# ProcurementOrder Model
class ProcurementOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    inventory_item = models.ForeignKey(Inventory, on_delete=models.CASCADE)  # Renamed to `inventory_item`
    order_quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ])

    def __str__(self):
        return f"Order {self.id} - {self.inventory_item.product.product_name}"


# DemandForecasting Model
class DemandForecasting(models.Model):
    inventory_item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    forecasted_demand = models.PositiveIntegerField()
    forecast_date = models.DateTimeField()

    def __str__(self):
        return f"Forecast for {self.inventory_item.product.product_name} on {self.forecast_date}"