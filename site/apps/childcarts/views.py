from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from apps.products.models import Category
from .models import ChildCarts

class ChildCartListView(ListView):
    '''
        Displays a list of all available childcarts
    '''
    def get(self, request, *args, **kwargs):
        # all child carts have childcart as parent category. Therefore, we will
        # filter all categories which have childcart as parent
        categories = Category.objects.filter(parent_category__name__iexact='childcarts')
        context = {
            'childcart_list': ChildCarts.objects.filter(available=True),
            'category': None,
            'categories': categories,
        }
        return render(request, 'childcarts/childcart_list.html', context)


class ChildCartDetailView(DetailView):
    '''
        Display the details of a selected child cart
    '''
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(ChildCarts,
                                    id=kwargs['cart_id'],
                                    slug=kwargs['cart_slug'],
                                    available=True)
        # cart_product_form = CartAddProductForm()
        return render(request,
                      'childcarts/childcart_detail.html',
                      {
                          'product': product,
                          # 'cart_product_form': cart_product_form
                      }
                      )
