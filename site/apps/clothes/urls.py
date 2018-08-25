from django.urls import path

from .views import ClothDetailView, ClothesView, IndexView, ClothesListView

app_name = 'clothes'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clothes/',
         ClothesView.as_view(),
         name='clothes'),
    path('clothes-list/',
         ClothesListView.as_view(),
         name='clothes_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:cloth>/',
         ClothDetailView.as_view(),
         name='cloth_detail'),
]
