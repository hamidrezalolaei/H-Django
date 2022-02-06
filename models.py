from django.db import models

from django.contrib.auth.models import User  

# 1

STATUS_CHOICES = (          # used for dropdown. tuples are better since they are immutable
    ('NEW', 'New Site'),    # first value : saved to database, second value : human-readable name
    ('EX', 'Existing Site')
)

PRIORITY_CHOICES = (    # used for dropdown
    ('U', 'Urgent - 1 week or less'),
    ('N', 'Normal - 2 to 4 week'),
    ('L', 'Low - Still Researching'),
)

class Quote(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=60, blank=True)
    company = models.CharField(max_length=60, blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    web = models.URLField(blank=True)
    description = models.TextField()
    sitestatus = models.CharField(max_length = 20, choices = STATUS_CHOICES) # 'choice' : using select widget to display a drop-list poplulated with STATUS_CHOICE
    priority = models.CharField(max_length = 20, choices = PRIORITY_CHOICES) # same is up
    jobfile = models.FileField(upload_to = 'uploads/', blank=True) # used to upload a file into a folder
    submitted = models.DateField(auto_now_add=True) # automatically saves the current date and time in the submitted field.
    quotedate = models.DateField(blank=True, null=True) # *Django never sets a datefield to blank, to allow quotedata filed to be empty, null attribute needs also to set to True
    quoteprice = models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE) #empty values are not allowed for foreign keys, CACADE deletes all related entries in other tables

    def __str__(self):
        return str(self.id)
