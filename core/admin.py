from django.contrib import admin
from .models import JustSending, OrderItem, Coupon, SizeVariant, OrderItemProduct, ColorClassVariant, ColorVariant
from unfold.admin import ModelAdmin

class OrderItemProductAdmin(ModelAdmin):
    list_display = ['product', 'size', 'quantity', 'order_item_first_name', 'order_item_last_name', 'order_item_email']
    list_select_related = ['order_item']

    def order_item_first_name(self, obj):
        return obj.order_item.firstName

    def order_item_last_name(self, obj):
        return obj.order_item.lastName

    def order_item_email(self, obj):
        return obj.order_item.email

    order_item_first_name.short_description = 'First Name'
    order_item_last_name.short_description = 'Last Name'
    order_item_email.short_description = 'Email'

# Register each model with its respective admin
@admin.register(JustSending)
class JustSendingAdmin(ModelAdmin):
    pass

# @admin.register(DefaultSize)
# class DefaultSizeAdmin(ModelAdmin):
#     pass

# @admin.register(DefaultProductType)
# class DefaultProductTypeAdmin(ModelAdmin):
#     pass



@admin.register(SizeVariant)
class SizeVariantAdmin(ModelAdmin):
    pass

@admin.register(ColorClassVariant)
class ColorClassVariantAdmin(ModelAdmin):
    pass

@admin.register(ColorVariant)
class ColorVariantAdmin(ModelAdmin):
    pass

@admin.register(Coupon)
class CouponAdmin(ModelAdmin):
    pass

@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    pass

# Register the custom admin for OrderItemProduct
@admin.register(OrderItemProduct)
class CustomOrderItemProductAdmin(OrderItemProductAdmin):
    pass


