import requests
import os

import requests
import os

import random

from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, TemplateView

from .models import PromotionalVideo, Cart
from .get_products_list import get_products_list
from .constants import shop_code_to_shop_image_url_dict

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

class PromotionalVideoListView(ListView):
    model = PromotionalVideo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filtered_shop_stories = []
        for promotional_video in context['promotionalvideo_list']:
            if promotional_video.shop_code in shop_code_to_shop_image_url_dict:
                filtered_shop_stories.append({
                    'promotional_video_id': promotional_video.id,
                    'image_url': shop_code_to_shop_image_url_dict[promotional_video.shop_code],
                    'shop_code': promotional_video.shop_code,
                })

        context['shop_stories'] = filtered_shop_stories

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
        for i, product in enumerate(products):
            if i==0:
                product['random_float'] = 1
            else:
                product['random_float'] = random.random()
            review = round(product['reviewAverage'])
            if review == 0:
                review += 1
            product['reviewAverage'] = list(range(review))

        context['products'] = products
        random_float_list = [random.random() for _ in range(len(products))]
        random_float_list[0] = 1
        context['random_float_list'] = random_float_list
        return context
