from django.db import models

from apps.products.models import Product


class ChildCarts(Product):
    '''
    ChildCarts is a base category which will store different types of carts
    e.g. Barnevogne, kombi/duovogn, klapvogn, lobejogere,
    '''
    age_group = models.CharField(max_length=200)
    # l/w/h are declared as CharFields because they have to store below values
    # Total bredde på stel med hjul: 56 cm
    # Stel sammenklappet uden hjul: 84 / 47 / 18 cm
    # Barnevognskasse (indvendig): 98 / 38 / 23 cm
    # Styrets højde (laveste - højeste): 92 - 116 cm
    length = models.CharField(max_length=200, blank=True, null=True)
    width = models.CharField(max_length=200, blank=True, null=True)
    height = models.CharField(max_length=200, blank=True, null=True)
    # Example values for weight are below
    # Stel inkl. Hjul: 10,8 kg
    # Barnevognskasse : 6.7 kg
    weight = models.CharField(max_length=200, blank=True, null=True)

