from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView

from .models import Quote
from .forms import QuoteForm
from pages.models import page

# 4

class QuoteList(ListView):
    model = Quote
    context_object_name = 'all_quotes'

def quote_req(request):
    submitted = False
    if request.method == "POST":
        form = QuoteForm(request.POST, request.FILES) # FILES to retrieve file upload information from the response
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/quote/?submitted=True')
    else : 
        form = QuoteForm()
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'quotes/quote.html', {'form' : form, 'page_list': page.objects.all(), 'submitted' : submitted})

