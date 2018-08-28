from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import View, ListView, DetailView

from .models import Clothes
from apps.products.models import Category

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pages/index.html', {})
        # return HttpResponse("Hello, world. You're at the clothing index.")


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


class ClothesListView(ListView):

    def get(self, request, *args, **kwargs):
        try:
            clothes_list = Clothes.objects.all().order_by('-created')
        except Clothes.DoesNotExist:
            raise Http404("No clothes in the stock")
        ## FIXME
        ## TODO pagination is not working,
        # paginator = Paginator(clothes_list, 3) # 3 posts in each page
        # page = request.GET.get('page')
        # try:
        #     clothes = paginator.page(page)
        # except PageNotAnInteger:
        #     # If page is not an integer deliver the first page
        #     clothes = paginator.page(1)
        # except EmptyPage:
        #     # If page is out of range deliver last page of results
        #     clothes = paginator.page(paginator.num_pages)
        # return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})
        # paginate_by =3
        context = {
            'categories': Category.objects.all(),
            'page': request.GET.get('page'),
            'clothes_list': clothes_list,
        }
        return render(request, 'clothes/clothes_list.html', context)


class ClothDetailView(DetailView):

    def get(self, request, *args, **kwargs):
        cloth = get_object_or_404(
            Clothes,
            created__year=kwargs['year'],
            created__month=kwargs['month'],
            created__day=kwargs['day'],
            slug=kwargs['cloth'],
        )

        context = {
            'cloth': cloth
        }
        return render(request, 'clothes/clothes_detail.html', context)
