from django.contrib import admin
from .models import UserProfile, Product, Category, Inventory, ProcurementOrder, Supplier

# Import required for displaying images in admin
from django.utils.html import format_html


# Register UserProfile model
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_active', 'is_admin')
    search_fields = ('email', 'username')
    list_filter = ('is_admin', 'is_active')
    
# Register Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name')
    list_filter = ('created_at')

# Register Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock', 'created_at', 'display_image')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'created_at')
    
    def dispaly_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height: 45px;"/>'.format(obj.image.url))
        return "No Image"
    
# Register Inventory    
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'reorder_level', 'last_updated')
    search_fields = ('product__name')
    list_filter = ('last_updated')
    
# Register Supplier model
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

# Register   ProcurementOrder model
@admin.register(ProcurementOrder)
class ProcurementOrderAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'inventory_item', 'order_quantity', 'order_date', 'status')
    search_fields = ('supplier__name', 'inventory_item__product__name')
    list_filter = ('status', 'order_date')

# Register DemandForecasting model
@admin.register(DemandForecasting)
class DemandForecastingAdmin(admin.ModelAdmin):
    list_display = ('inventory_item', 'forecasted_demand', 'forecast_date')
    search_fields = ('inventory_item__product__name')
    list_filter = ('forecast_date')
    
