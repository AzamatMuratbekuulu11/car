from django.urls import path
from .views import ShopListView, ShopDetailView, ShopCreateView, ShopUpdateView, ShopDeleteView

urlpatterns = [
    path('', ShopListView.as_view(), name="shop_list"),
    path('<int:pk>/', ShopDetailView.as_view(), name="shop_detail"),
    path('create/', ShopCreateView.as_view(), name="shop_create"),
    path('<int:pk>/update/', ShopUpdateView.as_view(), name="shop_update"),
    path('<int:pk>/delete/', ShopDeleteView.as_view(), name="shop_delete"),
]