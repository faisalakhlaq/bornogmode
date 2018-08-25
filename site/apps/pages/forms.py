from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        # no need for this method, EmailField will do the necessary checks
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        if not email_base or not domain or not extension:
            raise forms.ValidationError("Please provide a valid email")
        return email


class SearchForm(forms.Form):
    text = forms.CharField(max_length=100)
