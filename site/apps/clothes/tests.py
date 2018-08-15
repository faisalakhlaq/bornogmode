from django.test import TestCase
from django.urls import reverse

from .models import Clothes


def create_cloth(name, size, price):
    return Clothes.objects.create(name=name, size=size, price=price)


class ClothesIndexViewTests(TestCase):

    def test_index_view(self):
        response = self.client.get(reverse(''))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world. You're at the clothing index.")

    def test_clothes_view(self):
        create_cloth('asd','2',2000)
        create_cloth('qweq','1',1500)

        response = self.client.get(reverse('/clothes/'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['clothes_list'],
            ['<Clothes: asd, 2, 2000>', '<Clothes: qweq, 1, 1500>']
        )
