from django.db import models


class Clothes(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # name of the clothes
    name = models.CharField(max_length=150, null=True)
    # size of the clothes
    size = models.CharField(max_length=50, null=True)
    # these clothes suit this age group
    age_group = models.CharField(max_length=50, null=True)
    # how many sms are sent
    colour = models.CharField(max_length=50, null=True)
    # cost incurred for sending all the sms
    price = models.DecimalField(
        max_digits=12, decimal_places=5, default=0.0)
    brand_name = models.CharField(max_length=50, null=True)
    # these clothes are worn in which season
    season = models.CharField(max_length=50, null=True)
    # which category these lothes belong to, e.g sleeping dress, swimming dress,
    # shirts, tops, bottoms
    category = models.CharField(max_length=50, null=True)

    def __str__(self):
        return "Name: {}, \n Size: {}, \n Age Group: {}, \n Colour: {}" \
               "\n Price: {}, \n Brand Name: {}, \n Season: {}, " \
               "\n Category: {}".format(
            self.name, self.size, self.age_group, self.colour, self.price,
            self.brand_name, self.season, self.category
        )

