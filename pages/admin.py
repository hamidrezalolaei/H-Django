from django.contrib import admin
# a model should be  registered with the admin to be accessible from the admin
from .models import page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('title',)
    search_fields = ('title',)

admin.site.register(page, PageAdmin)

# Register your models here.
