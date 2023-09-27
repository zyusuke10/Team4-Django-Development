from typing import Any
from django.shortcuts import get_object_or_404, redirect
from .models import PromotionalVideo, Cart
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, ListView, DetailView

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

