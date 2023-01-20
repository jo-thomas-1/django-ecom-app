from django.urls import path
from . import views # importing views module from current folder

app_name = "cart"

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('delete/<int:product_id>/', views.delete_cart, name='delete_cart'),
    path('', views.cart_details, name='cart_details')
]