from django.db import models # as a default because of using startapp

class page(models.Model): # must be inheriter for Django's Model class
    title = models.CharField(max_length=60) # <title></title>
    permalink = models.CharField(max_length=12, unique=True) # a permalink to an individual page
    update_date = models.DateTimeField('Last Updated') # when was the page last updated - keep track of page edits
    body_text = models.TextField('Page Content', blank=True) # the HTML content of the page. this is put in <body></body> element of the template.
    # TextField is a large text field that can hold many thousand of characters

    def __str__(self):
        return self.title

# Create your models here.
