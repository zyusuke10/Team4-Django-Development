from django.urls import path

from . import views

app_name = 'team_4_app'
urlpatterns = [
    path('promotional-video/', views.PromotionalVideoListView.as_view(), name='promotional_video_list'),
]
