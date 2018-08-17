from django.urls import path

from .views import HomePageView, AboutUsView, ContactFormView, home_files


app_name = 'pages'

urlpatterns = [
    path('<filename>(robots.txt)|(humans.txt))',
        home_files, name='home-files'),
]

urlpatterns += [
    path('',
         HomePageView.as_view(),
         name='home'),
    path('contact-us/',
         ContactFormView.as_view(),
         name='contact_us'),
    path('about-us/',
         AboutUsView.as_view(),
         name='about_us'),
]
