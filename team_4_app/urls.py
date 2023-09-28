from django.urls import path

from . import views

app_name = 'team_4_app'
urlpatterns = [
    path('checkout/', views.CartListView.as_view(), name='checkout'),
    path('promotional-video/', views.PromotionalVideoListView.as_view(), name='promotional-video-list'),
    path('promotional-video/<int:pk>', views.PromotionalVideoDetailView.as_view(), name='promotional-video-detail'),
    path('delete_item_from_cart/<int:pk>/<str:product_id>/', views.delete_item_from_cart, name='delete_item_from_cart'),
    path('product_list', views.ProductListView.as_view(), name='product_list'),
]
