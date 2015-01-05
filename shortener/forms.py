from django import forms

from .models import Link

class LinkCreationForm(forms.Form):
    link = forms.URLField(label='url to be shortened')



