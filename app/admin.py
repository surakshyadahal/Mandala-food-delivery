from django.contrib import admin

from app.models import (Banner, Customer, Food, FoodCategory, Notification, Order, OrderItem,
    OrganizationSetting, Rating, Restaurant)

# Register your models here.
@admin.register(OrganizationSetting)
class OrganizationSettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'currency')
    

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'category', 'restaurant', 'type')
    

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','phone', 'email', 'address', 'is_active')


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('customer', 'status', 'address', 'destination_phone', 'sub_total', 'delivery_charge', 'total', )
    
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'food', 'star', 'review', 'is_active')
    
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'url')