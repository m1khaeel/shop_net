from rest_framework import serializers
from catalog.models import Category, Producer, Discount, Promocode, Product, Order, OrderProducts
from datetime import date

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class ProducerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producer
        fields = ('id', 'name', 'description', 'country' )


class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = ('id', 'name', 'percent', 'date_start', 'date_end' )

class PromocodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promocode
        fields = ('id', 'name', 'percent', 'date_start', 'date_end', 'is_cumulative' )


class ProductSerializer(serializers.ModelSerializer):
    discount = DiscountSerializer()
    category = CategorySerializer()
    producer = ProducerSerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'count_on_stock', 'articul',
                  'description', 'discount', 'category', 'producer')


class ProductInBasketSerializer(serializers.Serializer):
     name = serializers.CharField()
     price = serializers.DecimalField(max_digits=15, decimal_places=2)
     number_of_items = serializers.IntegerField()
     # discount = DiscountSerializer()

class BasketSerializer(serializers.Serializer):
    products = ProductInBasketSerializer(many=True)
    result_price = serializers.SerializerMethodField()

    def get_result_price(self, data):
        result_price = 0
        for item in data.get('products'):
            if item.get('discount'):
                percent = item.get('discount_percent')
                date_end = item.get('discount_date_end')
                delta = date.today() - date_end
                if delta.days <= 0:
                    result_price += (item.get('price') * (100 - percent) / 100) * item.get('number_of_items')
                else:
                    result_price += item.get('price') * item.get('number_of_items')
            else:
                result_price += item.get('price') * item.get('number_of_items')

        return result_price

class AddProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    number_of_items = serializers.IntegerField()

class DeleteProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()

class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProducts
        fields = ("products", "count")

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['date_created', 'promocode', 'delivery_time', 'delivery_notif_in_time', 'delivery_method',
                  'delivery_status', 'delivery_address', 'payment_method', 'payment_status', 'user',
                  'result_price', 'products']
        read_only_fields = ['date_created', 'delivery_status',
                            'payment_status', 'result_price']

    def create(self, validated_data):
        pass

