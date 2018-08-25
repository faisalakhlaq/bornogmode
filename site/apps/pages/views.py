from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from django.contrib.postgres.search import SearchVector

from .forms import ContactForm, SearchForm
from apps.clothes.models import Clothes
from apps.brands.models import Brand

def home_files(request, filename):
    '''
    Method to return robot.txt and humans.txt
    '''
    return render(request, filename, {}, content_type="text/plain")


class SearchTextView(View):

    def get_context(self, request, clothes_list=None, search_results=False, *args, **kwargs):
        context = {
            'form': SearchForm,
            'clothes_list': clothes_list,
            'search_results': search_results,
        }
        return context

    def get(self, request, *args, **kwargs ):
        # context = {
        #     'form': SearchForm,
        # }
        context = self.get_context(request, args, kwargs)
        template = "pages/search_page.html"
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        search_form = SearchForm(request.POST or None)

        if not search_form.is_valid():
            self.get(request, args, kwargs)

        search_text = search_form.cleaned_data.get("text")
        searched_clothes = Clothes.objects.annotate(
            search=SearchVector('name', 'category'),
        ).filter(search=search_text)
        # TODO FIXME brand name search for Me TOO is not working
        searched_brands = Brand.objects.annotate(
            search=SearchVector('name', 'company_name'),
        ).filter(search=search_text)
        searched_brand_clothes = []
        if searched_brands:
            if searched_clothes:
                searched_brand_clothes += Clothes.objects.\
                    filter(brand_name__in=searched_brands).\
                    exclude(searched_clothes)
            else:
                searched_brand_clothes += Clothes.objects.\
                    filter(brand_name__in=searched_brands)

        searched_brand_clothes += list(searched_clothes)
        # context = {
        #     'form': SearchForm,
        #     'clothes_list': searched_brand_clothes,
        #     'search_results': True,
        # }
        context = self.get_context(request, searched_brand_clothes, True, args, kwargs)
        template = "pages/search_page.html"
        return render(request, template, context)


class ErrorPageView(View):
    error_code = None
    def get(self, request, *args, **kwargs):
        error_pages = {
            '404': 'errorpages/404.html',
            '403': 'errorpages/403.html',
            '400': 'errorpages/400.html',
            '500': 'errorpages/500.html',
        }
        template = error_pages.get(self.error_code)
        return render(request, template, {})


class HomePageView(View):

    def get(self, request, *args, **kwargs):
        contactus_form = ContactForm()
        context = {
            'form': contactus_form,
        }
        return render(request, 'pages/index.html', context)

    def post(self, request, *args, **kwargs):
        # TODO
        view = ContactFormView()
        return view.post(request, args, kwargs)


class AboutUsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'pages/about_us.html', {})


class ContactFormView(View):
    title = 'Contact Us'

    def get(self, request, *args, **kwargs):
        contactus_form = ContactForm()
        context = {
            'title': self.title,
            'form': contactus_form,
        }
        return render(request, 'pages/contact_us.html', context)

    def post(self, request, *args, **kwargs):
        contact_us_form = ContactForm(request.POST or None)
        if contact_us_form.is_valid():
            print(contact_us_form.cleaned_data)
            full_name = contact_us_form.cleaned_data.get("full_name")
            to_email = contact_us_form.cleaned_data.get("email")
            message = contact_us_form.cleaned_data.get("message")
            subject = "Contact us form"
            contact_message = "%s: %s via %s"%(
                full_name,
                message,
                to_email
            )

            send_mail(
                subject, # 'Subject',
                contact_message, # message',
                settings.CONTACTUS_FORM_EMAIL, # 'from@example.com',
                [to_email],# ['to@example.com'],
                fail_silently=False,
            )

        context = {
            'title': self.title,
            'form': contact_us_form,
        }
        return render(request, 'pages/contact_us.html', context)
