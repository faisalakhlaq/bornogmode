from django.db import models

from apps.utils.models import Address


class Brand(models.Model):
    '''Keep the details for different brands'''
    name = models.CharField(max_length=150, blank=False, null=False)
    company_name = models.CharField(max_length=150, blank=True, null=True,)
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        blank=True,
        null=True)

    def __str__(self):
        return self.name
