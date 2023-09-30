from django.urls import path

from . import views

app_name = 'team_4_app'
urlpatterns = [
    path('cart/', views.CartListView.as_view(), name='cart'),
    path('cart/<int:pk>/delete', views.CartDeleteView.as_view(), name='cart_delete_item'),
    path('checkout/', views.CheckoutListView.as_view(template_name='team_4_app/checkout_list.html'), name='checkout'),
    path('promotional-video/', views.PromotionalVideoListView.as_view(), name='promotional_video_list'),
    path('promotional-video/<int:pk>', views.PromotionalVideoDetailView.as_view(), name='promotional_video_detail'),
    path('product-list/', views.ProductListView.as_view(), name='product_list'),
    # path('delete_item_from_cart/<int:pk>/<str:product_id>/', views.delete_item_from_cart, name='delete_item_from_cart'),
]
