from django.contrib import admin
from .models import Quote

# 2

class QuoteAdmin(admin.ModelAdmin):  # now what the fuck is this?
    list_display = ('id', 'name', 'company', 'submitted', 'quotedate', 'quoteprice')
    list_filter = ('submitted', 'quotedate')
    readonly_fields = ('submitted',) # because it is a readonly and "auto_now_add=True" if not: Error
    fieldsets = (  # setting collapsible grouping, controls the layout of the add and edit pages in admin
        (None, {  # when None: the no group title will be shown
            'fields' : ('name', 'email', 'description')
        }),
        ('Contact Information', {      # two tuples : (<Name>, <fields_options>)
            'classes' : ('collapse',),  # collapse is a special built-in class that uses JavaScript to apply an accordion to a set of fields
            'fields' : ('position', 'company', 'address', 'phone', 'web')
        }),
        ('Job Information', {
            'classes' : ('collapse',), 
            'fields' : ('sitestatus', 'priority', 'jobfile', 'submitted')
        }),
        ('Quote Admin', {
            'classes' : ('collapse',),
            'fields' : ('quotedate', 'quoteprice', 'username')
        }),
    )


admin.site.register(Quote, QuoteAdmin)

# from now on :
# create the QuoteForm model form for collecting the quote request information from the user
# Add a new view to manage the forms
# Create the form template
# add ournew view and form to urls.py file and update the site template to link the quote form
