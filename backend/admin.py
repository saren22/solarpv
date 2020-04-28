from django.contrib import admin
from . import models

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display= ('model_number', 'product_name', 'cell_technology', 'cell_manufacturer', 'number_of_cells', 'number_of_diodes', 'superstate_type')
    list_display_links = None
    list_per_page = 5
    actions_on_top = False
    list_filter= ('model_number', 'product_name')
    search_fields= ('model_number', 'product_name')

class ClientAdmin(admin.ModelAdmin):
    list_display= ('client_id', 'client_name', 'client_type', 'client_code')
    list_filter= ('client_id', 'client_name')
    fields = (('client_id','client_type'), ('client_name','client_code'))


class LocationAdmin(admin.ModelAdmin):
    list_display= ('location_id', 'address_1', 'city', 'country', 'phone_number', 'state', 'client_id')
    list_filter= ('location_id' ,'city')


class Test_StandardAdmin(admin.ModelAdmin):
    list_display= ('standard_id', 'standard_name', 'description', 'published_date')
    list_filter= ('standard_id', 'standard_name')


class CertificateAdmin(admin.ModelAdmin):
    list_display= ('certificate_number', 'id', 'user_id', 'report_number', 'issue_date', 'location_id', 'model_number')
    list_filter= ('certificate_number', 'user_id')

    
 
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Test_Standard, Test_StandardAdmin)
admin.site.register(models.Certificate, CertificateAdmin)

