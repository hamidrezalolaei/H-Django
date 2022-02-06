from django import forms
from django.forms import ModelForm
from .models import Quote

# 3

class QuoteForm(ModelForm):
    required_css_class = 'required' # adds a CSS class to our required fields -->  #  used to add an asterisk to the required fields in the form template
    class Meta:  # used to pass in the metadata options the ModelForm class needs to render the form.// note : it is Meta
        model = Quote # the model to base the form on
        fields = [  # model fields to render on the form
            'name', 'position', 'company', 'address',
            'phone', 'email', 'web', 'description',
            'sitestatus', 'priority', 'jobfile'
        ]