from django.urls import path
from . import views

app_name = 'team_4_app'
urlpatterns = [
    path('checkout/',views.CartListView.as_view(),name='checkout'),
]