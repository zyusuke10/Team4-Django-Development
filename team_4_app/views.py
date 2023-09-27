from .models import Cart
from django.views.generic import ListView
import requests
import os

# Create your views here.

class CartListView(ListView):
    model = Cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = list(context['object_list'].values_list('product_id', flat=True))
        product_info_list = []
        
        rakuten_api_endpoint = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601?"
        rakuten_applicationId = os.getenv('APPLICATION_ID')
        
        for cart_item in cart_items:
            product_id = cart_item
            params = {
                    'applicationId':rakuten_applicationId,
                    'itemCode': product_id, 
            }
            response = requests.get(rakuten_api_endpoint,params=params)

            if response.status_code == 200:
                product_info = response.json()
                product_info_list.append(product_info)
                
        context['product_info_list'] = product_info_list
        print(product_info_list)
        
        return context
