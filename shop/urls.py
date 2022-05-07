from django.urls import path
from .views import checkout, home, shop, cart, updateItem, processOrder

urlpatterns = [
        path('home', home, name="home"),
        path('shop/', shop, name="shop"),
        path('checkout/', checkout, name="checkout"),
        path('cart/', cart, name="cart"),
        path('update_item/', updateItem, name="update_item"),
        path('process_Order/', processOrder, name="process_Order"),
        
        
        
]