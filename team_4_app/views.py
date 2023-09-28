import requests
import os

from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from urllib.parse import urljoin, urlparse

from .models import PromotionalVideo, Cart
from .get_products_list import get_products_list
from .constants import shop_code_to_shop_image_url_dict
from .apis import get_products_by_product_ids, get_products_by_shop_code

class CartListView(ListView):
    model = Cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_info_list'] = get_products_by_product_ids(context['object_list'])
        return context

class CartDeleteView(DeleteView):
    model = Cart
    template_name = 'team_4_app/cart_delete.html'
    success_url = reverse_lazy('team_4_app:cart')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = get_products_by_product_ids([context['object']])
        context['product'] = None
        if len(products) > 0:
            context['product'] = products[0]
            
            # Get full size image url by removing querystring from url
            medium_image_url = context['product']['mediumImageUrls'][0]
            context['product']['image_url'] = urljoin(medium_image_url, urlparse(medium_image_url).path)

        return context

class CheckoutListView(ListView):
    model = Cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['product_info_list'] = get_products_by_product_ids(context['object_list'])
        context['total_price'] = 0

        for product in context['product_info_list']:
            itemPrice = product["Items"][0]["Item"]["itemPrice"]
            context['total_price'] += itemPrice
                
        context['order_total'] = context['total_price']
        context['total_price'] += 400 #Constant shipping fee

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
        context['products'] = products
        return context
