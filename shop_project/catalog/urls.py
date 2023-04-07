from django.urls import path
from catalog.views import  ProducerListView, DiscountListView, PromocodetListView, \
    ProductListView, CategoryView, ProducerProductsView, DiscountProductsView

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<int:category_id>/', CategoryView.as_view(), name='category-products'),

    path('producers/', ProducerListView.as_view()),
    path('producers/<int:producer_id>/', ProducerProductsView.as_view(), name='producer-products'),

    path('discounts/', DiscountListView.as_view()),
    path('discounts/<int:discount_id>/', DiscountProductsView.as_view(), name='discount-products'),
    path('promocodes/', PromocodetListView.as_view()),
    path('products/', ProductListView.as_view()),

]
