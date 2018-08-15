from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import View, ListView, DetailView

from .models import Clothes


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, world. You're at the clothing index.")


class ClothesView(ListView):

    def get(self, request, *args, **kwargs):
        try:
            clothes = Clothes.objects.all()
        except Clothes.DoesNotExist:
            raise Http404("No clothes in the stock")

        context = {
            'clothes_list': clothes,
        }
        return render(request, 'clothes/clothes.html', context)


class ClothDetailView(DetailView):

    def get(self, request, *args, **kwargs):
        cloth = get_object_or_404(Clothes, name=kwargs['name'])

        context = {
            'cloth': cloth
        }
        return render(request, 'clothes/cloth_detail.html', context)
