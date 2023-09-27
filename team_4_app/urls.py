from django.urls import path
from . import views

app_name = 'team_4_app'
urlpatterns = [
    #path('test_detail/<int:pk>/', views.DetailTestView.as_view(), name='test_detail'),
    path('delete_item_from_cart/<int:pk>/<str:product_id>/', views.delete_item_from_cart, name='delete_item_from_cart'),
]