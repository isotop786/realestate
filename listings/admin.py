from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','list_date','realtor','is_published')
    list_display_links = ('id','title')

    list_editable = ['is_published',]

    list_filter = ['price']

    search_fields = ['title','city'] 
    # search_fields = ['realtor']

    list_per_page = 15
    



# Register your models here.
admin.site.register(Listing, ListingAdmin)