from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone','email','hire_date','is_mvp']
    list_display_links = ['id','name']

    list_editable = ['is_mvp']

    list_filter = ['hire_date']

    search_fields = ['name','phone']

    list_per_page = 10

# Register your models here.
admin.site.register(Realtor,RealtorAdmin)
