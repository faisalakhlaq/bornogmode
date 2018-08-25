from django.db import models
from django.urls import reverse

from apps.brands.models import Brand
from apps.products.models import Category


class Clothes(models.Model):
    SEASON_CHOICES = (
        ('summer', 'Summer'),
        ('winter', 'Winter'),
        ('spring', 'Spring'),
        ('winter', 'Winter'),
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # name of the clothes
    name = models.CharField(max_length=150, null=True, db_index=True)
    # size of the clothes
    size = models.CharField(max_length=50, null=True)
    # these clothes suit this age group
    age_group = models.CharField(max_length=50, null=True)
    # how many sms are sent
    colour = models.CharField(max_length=50, null=True)
    # cost incurred for sending all the sms
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    brand_name = models.ForeignKey(
        Brand,
        blank=True,
        null=True,
        related_name='clothes',
        on_delete=models.SET_NULL,
        # Prevent deletion of the referenced object by raising
        # ProtectedError, a subclass of django.db.IntegrityError??
    )
    # these clothes are worn in which season
    season = models.CharField(max_length=10,
                              choices=SEASON_CHOICES,
                              default='summer',)

    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        related_name='clothes',
        on_delete=models.SET_NULL)

    slug = models.SlugField(max_length=250, unique_for_date='created', db_index=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='clothes/%Y/%m',
                              blank=True)

    def __str__(self):
        return " Name: {}, \n Size: {}, \n Price: {} ".format(
            self.name, self.size, self.price
        )

    def get_absolute_url(self):
        # reverse() method allows to build URLs by their name and passing optional parameters.
        return reverse('clothes:cloth_detail',
                       args=[self.created.year,
                             self.created.month,
                             self.created.day,
                             self.slug])

    def get_clothes_description(self):
        return " Name: {}, \n Size: {}, \n Age Group: {}, \n Colour: {}" \
               "\n Price: {}, \n Brand Name: {}, \n Season: {}, " \
               "\n Category: {}".format(
            self.name, self.size, self.age_group, self.colour, self.price,
            self.brand_name, self.season, self.category
        )
