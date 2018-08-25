from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200)
    description = models.TextField(default='')
    # Any existing Category instance can be a parent_category.
    # To find all of the subcategories of a given Category
    # subcats = Category.objects.filter(parent_category__id=target_category.id)
    parent_category = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    class Meta:
        #Two categories under a parent cannot have same slug
        unique_together = ('slug', 'parent_category',)
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # all_slugs = [self.slug]
        # import pdb; pdb.set_trace()
        # if self.parent_category:
        #     all_slugs.append(self.parent_category.slug)
        # all_slugs = [self.slug]
        # p = self.parent_category
        # while p:
        #     all_slugs.append(p.slug)
        #     p = p.parent_category
        return reverse('products:product_list_by_category',
                       args=[self.id, self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('products:product_detail',
                           args=[self.id, self.slug])
