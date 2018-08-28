from django.urls import path

from .views import ChildCartListView, ChildCartDetailView

app_name = 'childcarts'

urlpatterns = [
    path('childcart-list/',
         ChildCartListView.as_view(),
         name='childcart_list'),
    path('',
         ChildCartListView.as_view(),
         name='childcart_list'),
    path('<category_name>',
         ChildCartListView.as_view(),
         name='childcart_category'),
    path('<int:cart_id>/<cart_slug>/',
         ChildCartDetailView.as_view(),
         name='childcart_detail'),

]
