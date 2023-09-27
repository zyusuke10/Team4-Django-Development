from typing import Any
from django.shortcuts import get_object_or_404, redirect
from .models import PromotionalVideo, Cart
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, DetailView
from .get_products_list import get_products_list

# Create your views here.
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

class ProductListView(TemplateView):
    model = Cart
    template_name = 'team_4_app/product_list.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        shop_code = self.request.GET.get(key='shop_code', default='grazia-doris')
        products = get_products_list(shop_code)
        context['products'] = products
        return context

class DetailTestView(DetailView):
    model = Cart
    template_name = 'team_4_app/test_detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        content = super().get_context_data(**kwargs)
        cart = content['cart']
        ids = cart.product_id
        ids = ids.split(',')
        content['cart'].product_id = ids
        return content