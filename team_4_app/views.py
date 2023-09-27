from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import PromotionalVideo
from .constants import shop_stories

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

