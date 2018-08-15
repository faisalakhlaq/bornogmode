from django.urls import path
# from django.conf.urls import url

from .views import ClothDetailView, ClothesView, IndexView
app_name = 'clothes'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clothes/',
         ClothesView.as_view(),
         name='clothes'),
    path('<name>/',
         ClothDetailView.as_view(),
         name='clothes_detail'),
    # url(r'^(?P<name>\w+)/$',
    #     ClothDetailView.as_view(),
    #     name='clothes_detail'),

]
