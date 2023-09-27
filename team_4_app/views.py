from django.shortcuts import render
from django.views.generic import ListView

from .models import PromotionalVideo

class PromotionalVideoListView(ListView):
    model = PromotionalVideo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop_stories'] = [
            {
                'image_url': 'https://www.rakuten.ne.jp/gold/rakutenmobile-store/assets/img/common/logo-rmobile-1line.svg?200424',
                'shop_code': 'rakutenmobile-store'
            },
            {
                'image_url': 'https://www.rakuten.ne.jp/gold/rakutenmobile-store/assets/img/common/logo-rmobile-1line.svg?200424',
                'shop_code': 'rakutenmobile-store'
            },
            {
                'image_url': 'https://www.rakuten.ne.jp/gold/rakutenmobile-store/assets/img/common/logo-rmobile-1line.svg?200424',
                'shop_code': 'rakutenmobile-store'
            },
            {
                'image_url': 'https://www.rakuten.ne.jp/gold/rakutenmobile-store/assets/img/common/logo-rmobile-1line.svg?200424',
                'shop_code': 'rakutenmobile-store'
            },
            {
                'image_url': 'https://static.vecteezy.com/system/resources/previews/010/994/232/non_2x/nike-logo-black-clothes-design-icon-abstract-football-illustration-with-white-background-free-vector.jpg',
                'shop_code': 'nike-official'
            }
        ]

        return context
