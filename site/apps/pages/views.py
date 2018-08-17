from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import View
from django.conf import settings

from .forms import ContactForm


def home_files(request, filename):
    '''
    Method to return robot.txt and humans.txt
    '''
    return render(request, filename, {}, content_type="text/plain")


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
