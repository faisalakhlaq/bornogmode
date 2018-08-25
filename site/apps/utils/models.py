from django.db import models


class Address(models.Model):
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    title = models.CharField(max_length=128, blank=True)

    street = models.CharField(max_length=128, blank=True)
    street_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, blank=True)
    postcode = models.CharField(max_length=128, blank=True)
    country = models.CharField(max_length=128, blank=True)

    phone = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=True)
