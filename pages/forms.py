from cProfile import label
from django import forms

class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label = 'Your name')
    email = forms.EmailField(required=False, label='Your Email address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

# to render on the website 
#      1. add the form to the list of URLs in the pages app
#      2. add navigation to the site template
#      3. Create a Template for the contact form
#      4. Create a new View to manage the contact form