from django import forms

from atmospheres_site.apps.base.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
