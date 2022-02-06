import django
from django.shortcuts import render, get_object_or_404 # used for rendering templates
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect # HTTP communication protocol, uses REQUEST and RESPONSE to transmit data between app and browser. We need a response object to pass view information back to the browser
from django.core.mail import send_mail, get_connection

from .models import page
from .forms import ContactForm

# def index(request): # view function --> takes a request from the web browser and returns a response. here is just a text formatted as HTML heading
#     #return HttpResponse("<h1>The Meandco Homepage</h1>")
#     return render(request, 'pages/page.html') # render is a special Django helper function that creates shortcut for communicating with web browser.
def index(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(page, permalink=pagename) # what is this function used for?
    context = { # populate a dictionary of items to pass to the template
        'title' : pg.title,
        'content' : pg.body_text, 
        'last_updated' : pg.update_date,
        'page_list' : page.objects.all(),
    }
    # assert False
    return render(request, 'pages/page.html', context=context)

# def error404(request):  # what the hell should i do for this here?
#     return HttpResponseNotFound('custom 404 not found')
def contact(request):
    submitted = False
    if request.method =='POST': # check if form was POSTed, if not create a blank form
        form = ContactForm(request.POST) # dunno what does this mean???
        if form.is_valid():
            cd = form.cleaned_data # normalize a data and creates a dictionary of the contents
            # assert False # to check the form works well
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'], 
                cd['message'],
                cd.get('email',
                'noreply@example.com'),
                ['siteowner@example.com'], connection = con
                )
            # when you enter valid data and submit the form, the contact view will redirect to the contact page with "submitted=True" as GET parameter
            # With "submitted=True" the contact.html template will execute the first {% if %} block and render the succss message of the form
            return HttpResponseRedirect('/contact?submitted=True') # redirect back to contact view, when submitted=True, instead of rendering the form the view will render the Thank you message

    else: 
        form = ContactForm()
        if 'submitted' in request.GET: # also what the fuck is this?
            submitted = True
    return render(request, 'pages/contact.html', {'form' : form, 'page_list': page.objects.all(), 'submitted' : submitted})