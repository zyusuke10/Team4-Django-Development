import requests
import os

import requests
import os

from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, TemplateView

from .models import PromotionalVideo, Cart
from .get_products_list import get_products_list
from .constants import shop_stories

# Create your views here.
class CartListView(ListView):
    model = Cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = list(context['object_list'].values_list('product_id', flat=True))
        product_info_list = []

        rakuten_api_endpoint = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601?'
        rakuten_applicationId = os.environ.get('APPLICATION_ID')

        total_price = 0

        for cart_item in cart_items:

            product_id = cart_item
            params = {
                'applicationId': rakuten_applicationId,
                'itemCode': product_id,
            }
            response = requests.get(rakuten_api_endpoint,params=params)

            if response.status_code == 200:
                product_info = response.json()
                product_info_list.append(product_info)

        for product in product_info_list:
            itemPrice = product["Items"][0]["Item"]["itemPrice"]
            total_price+=itemPrice
                
        context['product_info_list'] = product_info_list
        context['order_total'] = total_price
        context['total_price'] = total_price + 400 #Constant shipping fee

        return context

class ShopProductListView(TemplateView):
    template_name = 'team_4_app/shopproduct_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shop_code = self.kwargs['shop_code']

        rakuten_api_endpoint = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601?"
        rakuten_applicationId = os.environ.get('APPLICATION_ID')

        params = {
                    'applicationId':rakuten_applicationId,
                    'shopCode': shop_code,
            }
        response = requests.get(rakuten_api_endpoint,params=params)

        if response == 200:
            data = response.json()
            context['shop_data'] = data

        return context

@require_POST
def delete_item_from_cart(request, pk, product_id):
    print(request.POST)
    cart = get_object_or_404(Cart, pk=pk)
    ids = cart.product_id.split(',')
    #ids.remove(request.POST['product_id'])
    ids.remove(product_id)

    ids = ','.join(ids)
    cart.product_id = ids
    cart.save()

    return redirect('team_4_app:', pk=pk)

class ShopProductListView(TemplateView):
    template_name = 'team_4_app/shopproduct_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PromotionalVideoListView(ListView):
    model = PromotionalVideo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop_stories'] = shop_stories

        return context

class PromotionalVideoDetailView(DetailView):
    model = PromotionalVideo
    template_name = 'team_4_app/promotionalvideo_detail.html'

class ProductListView(TemplateView):
    model = Cart
    template_name = 'team_4_app/product_list.html'
    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        shop_code = self.request.GET.get(key='shop_code', default='grazia-doris')
        products = get_products_list(shop_code)
        context['products'] = products
        return context
