from django.urls import path

from . import views

app_name = 'team_4_app'
urlpatterns = [
    path('shop/<str:shop_code>', views.ShopProductListView.as_view(), name='shop-product-list'),
    path('promotional-video/', views.PromotionalVideoListView.as_view(), name='promotional-video-list'),
    path('promotional-video/<int:pk>', views.PromotionalVideoDetailView.as_view(), name='promotional-video-detail'),
]
