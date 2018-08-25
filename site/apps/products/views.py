from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# from cart.forms import CartAddProductForm


def product_list(request, id=None, slug=None, parent_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if slug and id:
        category = Category.objects.filter(slug=slug, id=id)
    elif slug and parent_slug:
        # TODO if a category if deleted and the product still has
        # this category then we will get into problem here
        # category = get_object_or_404(Category, slug=category_slug)
        category = Category.objects.filter(slug=slug, parent_category__slug=parent_slug)
    # elif slug:
    #         category = Category.objects.filter(slug=slug)

    if category:
            products = products.filter(category__in=category)
    return render(request,
                  'products/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  }
                  )


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    # cart_product_form = CartAddProductForm()
    return render(request,
                  'products/detail.html',
                  {
                      'product': product,
                      # 'cart_product_form': cart_product_form
                  }
                  )
