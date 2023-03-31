from django.contrib import admin
from catalog.models import Category, Discount, Promocode, Producer, Cashback, Product, Order, OrderProducts


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

class CashbackAdmin(admin.ModelAdmin):
    list_display = ('percent', 'threshold')

class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'percent', 'date_start', 'date_end')
    search_fields = ('name', 'percent')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'count_on_stock', 'articul', 'category', 'producer')
    search_fields = ('name', 'articul', 'category__name', 'producer__name')
    list_select_related = ('category', 'producer')

class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'percent', 'date_start', 'is_cumulative')
    search_fields = ('name', )

class OrderProductsInLine(admin.TabularInline):
    model = OrderProducts
    extra = 0
    readonly_fields = ('price', )

    def price(self, obj):
        return obj.product.price

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_created', 'delivery_time', 'user',
                     'result_price', 'delivery_status', 'payment_status')
    search_fields = ('id', 'user__email', )

    inlines = [OrderProductsInLine]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Cashback, CashbackAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Promocode, PromocodeAdmin)
admin.site.register(Order, OrderAdmin)



